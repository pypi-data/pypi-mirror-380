# All comments and code identifiers in English (as per your preference)
import re
import duckdb
import gzip
import io
import json
import logging
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Optional, Any

from nemo_library import NemoLibrary
from enum import Enum
from datetime import datetime


def _as_str(x: Any) -> str:
    return x.value if isinstance(x, Enum) else str(x)


def _slugify_filename(name: str | Enum) -> str:
    if isinstance(name, Enum):
        name = name.value
    s = str(name).strip().lower()
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^a-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_") or "table"


def _safe_table_name(name: str) -> str:
    """
    Convert an arbitrary name into a safe SQL identifier:
    - lowercase
    - replace all non-alphanumeric with underscores
    - collapse multiple underscores
    - strip leading/trailing underscores
    - ensure the name does not start with a digit (prefix with underscore if needed)
    """
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "table"
    if s[0].isdigit():
        s = "_" + s
    return s


def _is_gz(path: Path) -> bool:
    return str(path).lower().endswith(".gz")


@dataclass
class NDJSONRotation:
    rotate_every_n: Optional[int] = None  # rotate after N records
    rotate_max_bytes: Optional[int] = None  # rotate after file size (approx.)
    suffix_template: str = "{stem}.{part:05d}.ndjson"  # e.g. events.00001.ndjson


class ETLDuckDBHandler:
    """
    DuckDB + NDJSON helper to complement ETLFileHandler.
    - Streaming NDJSON writer (optionally gz)
    - Ingest NDJSON/NDJSON.GZ into DuckDB tables
    - Query helpers and Parquet export
    """

    def __init__(
        self,
        adapter: str | Enum,
    ):

        self.nl = NemoLibrary()
        self.config = self.nl.config
        self.logger = self._init_logger()

        etl_directory = self.config.get_etl_directory()
        if not etl_directory:
            raise RuntimeError("ETL directory is not configured (cfg.get_etl_directory())")
        warehouse_root = (
            Path(etl_directory) / (adapter.value if isinstance(adapter, Enum) else adapter) / "_warehouse"
        )
        warehouse_root.mkdir(parents=True, exist_ok=True)
        db_path = warehouse_root / "duckdb"
        self.db_path = str(db_path)

    # ---------- logger ----------

    def _init_logger(self) -> logging.Logger:
        logger_name = "nemo.etl.duckdb"
        logger = logging.getLogger(logger_name)
        if not logger.handlers:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(levelname)s %(name)s: %(message)s",
            )
        logger.info("Using standard Python logger for DuckDB handler.")
        return logger

    # ---------- path helpers (reuse ETL directory layout) ----------

    def _base_dir(
        self, adapter: str | Enum, step: str | Enum, substep: str | Enum | None
    ) -> Path:
        etl_dir = self.config.get_etl_directory()
        if not etl_dir:
            raise RuntimeError(
                "ETL directory is not configured (cfg.get_etl_directory())"
            )
        base = Path(etl_dir) / _as_str(adapter) / _as_str(step)
        if substep:
            base = base / _as_str(substep)
        base.mkdir(parents=True, exist_ok=True)
        return base

    def _ndjson_target(
        self,
        adapter: str | Enum,
        step: str | Enum,
        entity: str | Enum | None,
        filename: str | None,
        substep: str | Enum | None,
        gzip_enabled: bool,
    ) -> Path:
        base_dir = self._base_dir(adapter, step, substep)
        stem = _slugify_filename(filename or entity or "result")
        ext = ".ndjson.gz" if gzip_enabled else ".ndjson"
        return base_dir / f"{stem}{ext}"

    # ---------- NDJSON streaming writer ----------

    @contextmanager
    def streamNDJSON(
        self,
        adapter: str | Enum,
        step: str | Enum,
        entity: str | Enum | None,
        filename: str | None = None,
        gzip_enabled: bool = False,
        substep: str | Enum | None = None,
        rotation: Optional[NDJSONRotation] = None,
    ) -> Iterator["ETLDuckDBHandler._NDJSONWriter"]:
        """
        Context manager to stream NDJSON (one JSON object per line).
        Supports optional gzip and rotation by record count / size.
        """
        target = self._ndjson_target(
            adapter, step, entity, filename, substep, gzip_enabled
        )
        writer = self._NDJSONWriter(target, gzip_enabled, rotation, logger=self.logger)
        try:
            yield writer
        finally:
            writer.close()
            self.logger.info(
                f"NDJSON stream closed at {writer.current_path} (records_written={writer.total_records})."
            )

    class _NDJSONWriter:
        def __init__(
            self,
            path: Path,
            gzip_enabled: bool,
            rotation: Optional[NDJSONRotation],
            logger: logging.Logger,
        ):
            self.base_path = path
            self.gzip_enabled = gzip_enabled
            self.rotation = rotation
            self.logger = logger
            self.part = 1
            self.total_records = 0
            self._records_in_part = 0
            self._bytes_in_part = 0
            self._open_new_file()

        @property
        def current_path(self) -> Path:
            return self._path

        def _open_new_file(self):
            if self.rotation and (
                self.rotation.rotate_every_n or self.rotation.rotate_max_bytes
            ):
                stem = self.base_path.stem.replace(".ndjson", "").replace(
                    ".ndjson.gz", ""
                )
                suffix = self.rotation.suffix_template.format(stem=stem, part=self.part)
                self._path = self.base_path.with_name(suffix)
                if self.gzip_enabled and not _is_gz(self._path):
                    self._path = self._path.with_suffix(self._path.suffix + ".gz")
            else:
                self._path = self.base_path

            self._path.parent.mkdir(parents=True, exist_ok=True)
            if self.gzip_enabled:
                self._fh = gzip.open(self._path, "wb")
                self._write = lambda s: self._fh.write(s.encode("utf-8"))
            else:
                self._fh = open(self._path, "w", encoding="utf-8")
                self._write = lambda s: self._fh.write(s)

            self._records_in_part = 0
            self._bytes_in_part = 0
            self.logger.info(f"Opened NDJSON part {self.part} -> {self._path}")

        def _should_rotate(self) -> bool:
            if not self.rotation:
                return False
            if (
                self.rotation.rotate_every_n
                and self._records_in_part >= self.rotation.rotate_every_n
            ):
                return True
            if (
                self.rotation.rotate_max_bytes
                and self._bytes_in_part >= self.rotation.rotate_max_bytes
            ):
                return True
            return False

        def write_one(self, rec: dict) -> None:
            s = json.dumps(rec, ensure_ascii=False)
            line = s + "\n"
            self._write(line)
            self.total_records += 1
            self._records_in_part += 1
            self._bytes_in_part += len(line.encode("utf-8"))

            if self._should_rotate():
                self._fh.close()
                self.part += 1
                self._open_new_file()

        def write_many(self, recs: Iterable[dict]) -> None:
            for r in recs:
                self.write_one(r)

        def close(self):
            try:
                self._fh.close()
            except Exception:
                pass

    # ---------- DuckDB helpers ----------

    def _connect(self) -> duckdb.DuckDBPyConnection:
        return duckdb.connect(self.db_path)

    def ingest_ndjson(
        self,
        table: str,
        ndjson_paths: list[str | Path],
        create_table: bool = True,
        replace_table: bool = True,
        sampling_rows: int = 100000,
        slugify_table_name: bool = True,
    ) -> None:
        """
        Ingest one or more NDJSON/NDJSON.GZ files into DuckDB.

        - Uses read_json_auto(..., format='newline_delimited') for schema inference
        - If create_table and not exists -> CREATE TABLE AS SELECT
        - If replace_table -> DROP and recreate
        - Otherwise -> INSERT INTO ... SELECT ...
        - If slugify_table_name=True, the physical table name will be a safe SQL identifier
        (e.g., "Business relations" -> "business_relations"), preventing parser errors.
        """
        # Sanitize the physical table name to avoid SQL parser issues
        physical_table = _safe_table_name(table) if slugify_table_name else table

        con = self._connect()
        try:
            if replace_table:
                con.execute(f"DROP TABLE IF EXISTS {physical_table}")

            src_list = [str(Path(p)) for p in ndjson_paths]
            src_glob = ",".join([f"'{p}'" for p in src_list])

            # Create a VIEW for clean reuse
            con.execute(
                f"""
                CREATE OR REPLACE VIEW _v_src_json AS
                SELECT * FROM read_json_auto([{src_glob}],
                    format='newline_delimited',
                    sample_size={sampling_rows}
                );
            """
            )

            exists = bool(
                con.execute(
                    f"SELECT 1 FROM duckdb_tables() WHERE table_name = '{physical_table}'"
                ).fetchall()
            )

            if not exists and create_table:
                con.execute(
                    f"CREATE TABLE {physical_table} AS SELECT * FROM _v_src_json;"
                )
            else:
                con.execute(f"INSERT INTO {physical_table} SELECT * FROM _v_src_json;")

            con.execute("DROP VIEW _v_src_json;")
            self.logger.info(
                f"Ingested {len(src_list)} NDJSON files into table '{physical_table}' (logical='{table}')."
            )
        finally:
            con.close()

    def query_df(self, sql: str):
        con = self._connect()
        try:
            return con.execute(sql).fetchdf()
        finally:
            con.close()

    def copy_to_parquet(
        self, sql: str, parquet_path: str | Path, overwrite: bool = True
    ) -> Path:
        """
        Materialize a query into a Parquet file (ZSTD by default).
        """
        parquet_path = Path(parquet_path)
        parquet_path.parent.mkdir(parents=True, exist_ok=True)
        con = self._connect()
        try:
            if overwrite and parquet_path.exists():
                parquet_path.unlink()
            con.execute(
                f"COPY ({sql}) TO '{parquet_path}' (FORMAT PARQUET, COMPRESSION ZSTD);"
            )
            self.logger.info(f"Wrote Parquet: {parquet_path}")
            return parquet_path
        finally:
            con.close()

    def register_parquet_dir_as_view(
        self, view_name: str, directory: str | Path
    ) -> None:
        """
        Register all Parquet files in a directory as a DuckDB view (files can be partitioned).
        """
        con = self._connect()
        try:
            p = str(Path(directory))
            con.execute(
                f"CREATE OR REPLACE VIEW {view_name} AS SELECT * FROM read_parquet('{p}/**/*.parquet');"
            )
            self.logger.info(f"Registered view '{view_name}' over {p}")
        finally:
            con.close()

    def optimize_z_order(self, table: str, by_columns: list[str]) -> None:
        """
        Optional: Create a sorted copy to improve pruning. DuckDB doesn't have true Z-ORDER,
        but sorting can help for range filters.
        """
        con = self._connect()
        try:
            cols = ", ".join(by_columns)
            tmp = f"{table}__sorted_tmp"
            con.execute(f"DROP TABLE IF EXISTS {tmp}")
            con.execute(f"CREATE TABLE {tmp} AS SELECT * FROM {table} ORDER BY {cols}")
            con.execute(f"DROP TABLE {table}")
            con.execute(f"ALTER TABLE {tmp} RENAME TO {table}")
            self.logger.info(f"Optimized table '{table}' by sorting on {cols}.")
        finally:
            con.close()

    def execute_sql(self, sql: str) -> None:
        con = self._connect()
        try:
            con.execute(sql)
        finally:
            con.close()
