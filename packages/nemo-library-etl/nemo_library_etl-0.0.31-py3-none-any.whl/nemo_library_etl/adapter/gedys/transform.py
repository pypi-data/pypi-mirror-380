"""
Gedys ETL Transform Module.

This module handles the transformation phase of the Gedys ETL pipeline.
It processes the extracted data, applies business rules, data cleaning, and formatting
to prepare the data for loading into the target system.

The transformation process typically includes:
1. Data validation and quality checks
2. Data type conversions and formatting
3. Business rule application
4. Data enrichment and calculated fields
5. Data structure normalization
6. Comprehensive logging throughout the process

Classes:
    GedysTransform: Main class handling Gedys data transformation.
"""

import math
import duckdb
from prefect import get_run_logger
from nemo_library_etl.adapter._utils.db_handler import ETLDuckDBHandler, _safe_table_name
from nemo_library_etl.adapter._utils.enums import ETLAdapter, ETLStep
from nemo_library_etl.adapter._utils.file_handler import ETLFileHandler
from nemo_library_etl.adapter._utils.recursive_json_flattener import (
    RecursiveJsonFlattener,
)
from nemo_library_etl.adapter._utils.sentiment_analyzer import SentimentAnalyzer
from nemo_library_etl.adapter.gedys.config_models import PipelineGedys
from nemo_library import NemoLibrary

from nemo_library_etl.adapter.gedys.enums import GedysTransformStep
import pandas as pd


class GedysTransform:
    """
    Handles transformation of extracted Gedys data.

    This class manages the transformation phase of the Gedys ETL pipeline,
    providing methods to process, clean, and format the extracted data for loading
    into the target system.

    The transformer:
    - Uses NemoLibrary for core functionality and configuration
    - Integrates with Prefect logging for pipeline visibility
    - Applies business rules and data validation
    - Handles data type conversions and formatting
    - Provides data enrichment and calculated fields
    - Ensures data quality and consistency

    Attributes:
        nl (NemoLibrary): Core Nemo library instance for system integration.
        config: Configuration object from the Nemo library.
        logger: Prefect logger for pipeline execution tracking.
        cfg (PipelineGedys): Pipeline configuration with transformation settings.
    """

    def __init__(self, cfg: PipelineGedys):
        """
        Initialize the GedysTransform instance.

        Sets up the transformer with the necessary library instances, configuration,
        and logging capabilities for the transformation process.

        Args:
            cfg (PipelineGedys): Pipeline configuration object containing
                                                          transformation settings and rules.
        """
        self.nl = NemoLibrary()
        self.config = self.nl.config
        self.logger = get_run_logger()
        self.cfg = cfg

        super().__init__()

    def transform(self) -> None:
        """
        Execute the main transformation process for Gedys data.

        This method orchestrates the complete transformation process by:
        1. Loading extracted data from the previous ETL phase
        2. Applying data validation and quality checks
        3. Performing data type conversions and formatting
        4. Applying business rules and logic
        5. Creating calculated fields and data enrichment
        6. Ensuring data consistency and integrity
        7. Preparing data for the loading phase

        The method provides detailed logging for monitoring and debugging purposes
        and handles errors gracefully to ensure pipeline stability.

        Note:
            The actual transformation logic needs to be implemented based on
            the specific Gedys system requirements and business rules.
        """
        self.logger.info("Transforming all Gedys objects")

        if self.cfg.transform.sentiment_analysis:
            self._sentiment_analysis()
        if self.cfg.transform.flatten:
            self._flatten()
        if self.cfg.transform.join:
            self._join()

    def _sentiment_analysis(self) -> None:
        self.logger.info("Performing sentiment analysis for Gedys objects")

        db = ETLDuckDBHandler(adapter=ETLAdapter.GEDYS)
        sentiment_analyzer = SentimentAnalyzer()
        
        batch_size = self.cfg.transform.sentiment_analysis_batch_size

        for table, model in self.cfg.extract.tables.items():
            if model.active is False:
                self.logger.info(f"Skipping inactive table: {table}")
                continue

            fields = model.sentiment_analysis_fields
            if not fields:
                self.logger.info(f"No sentiment fields configured for {table}. Skipping.")
                continue

            raw_table = f"{_safe_table_name(table)}_raw"
            out_table = f"{_safe_table_name(table)}_sentiment"

            # Check existence
            con = duckdb.connect(str(db.db_path))
            try:
                exists_raw = bool(con.execute(
                    "SELECT 1 FROM duckdb_tables() WHERE table_name = ?", [raw_table]
                ).fetchone())
            finally:
                con.close()

            if not exists_raw:
                self.logger.warning(f"No raw DuckDB table found for {table} ({raw_table}). Skipping.")
                continue

            # Prepare curated output table: clone schema, drop heavy HTML fields, add sentiment columns
            con = duckdb.connect(str(db.db_path))
            try:
                con.execute(f"DROP TABLE IF EXISTS {out_table}")
                con.execute(f"CREATE TABLE {out_table} AS SELECT * FROM {raw_table} LIMIT 0")
                # Drop original heavy fields in curated table (mirrors old behavior)
                for f in fields:
                    # If column does not exist, DuckDB will raise; guard with pragma
                    exists = bool(con.execute(
                        "SELECT 1 FROM duckdb_columns() WHERE table_name = ? AND column_name = ?",
                        [out_table, f]
                    ).fetchone())
                    if exists:
                        con.execute(f"ALTER TABLE {out_table} DROP COLUMN {f}")

                # Add sentiment columns
                for f in fields:
                    score_col = f"{f}__sentiment_score"
                    label_col = f"{f}__sentiment_label"
                    dist_col  = f"{f}__sentiment_distribution_json"
                    cnts_col  = f"{f}__sentiment_counts_json"

                    con.execute(f"ALTER TABLE {out_table} ADD COLUMN {score_col} DOUBLE")
                    con.execute(f"ALTER TABLE {out_table} ADD COLUMN {label_col} VARCHAR")
                    con.execute(f"ALTER TABLE {out_table} ADD COLUMN {dist_col}  VARCHAR")  # JSON as VARCHAR
                    con.execute(f"ALTER TABLE {out_table} ADD COLUMN {cnts_col}  VARCHAR")

                rowcount = con.execute(f"SELECT COUNT(*) FROM {raw_table}").fetchone()[0]
            finally:
                con.close()

            if rowcount == 0:
                self.logger.warning(f"No data in {raw_table}. Skipping.")
                continue

            total_batches = math.ceil(rowcount / batch_size)
            written_total = 0

            # Stream batches from raw table
            select_sql = f"SELECT * FROM {raw_table}"  # add ORDER BY <id> if you need deterministic order

            for b in range(total_batches):
                offset = b * batch_size
                con = duckdb.connect(str(db.db_path))
                try:
                    batch_df = con.execute(f"{select_sql} LIMIT {batch_size} OFFSET {offset}").fetch_df()
                finally:
                    con.close()

                if batch_df.empty:
                    continue

                records = batch_df.to_dict(orient="records")

                enriched = sentiment_analyzer.analyze_sentiment_batch(
                    records,
                    sentiment_analysis_fields=fields,
                    max_plain_len=512,
                    chunk_len=512,
                    add_distribution=True,
                    add_counts=True,
                    json_serialize_stats=True,
                )

                df_enriched = pd.DataFrame(enriched)

                # Ensure expected columns exist
                for f in fields:
                    for col in (
                        f"plain_html_{f.lower()}",
                        f"{f}__sentiment_label",
                        f"{f}__sentiment_score",
                        f"{f}__sentiment_distribution_json",
                        f"{f}__sentiment_counts_json",
                    ):
                        if col not in df_enriched.columns:
                            df_enriched[col] = None

                    # Ensure original heavy column is absent (we dropped it in out_table)
                    if f in df_enriched.columns:
                        df_enriched.drop(columns=[f], inplace=True)

                # Align to out_table columns and insert
                con = duckdb.connect(str(db.db_path))
                try:
                    out_cols = [r[0] for r in con.execute(f"DESCRIBE {out_table}").fetchall()]
                    present_cols = [c for c in out_cols if c in df_enriched.columns]

                    # If some columns from raw table are missing in df_enriched (e.g., lists/structs),
                    # add them with None to keep the schema consistent
                    for c in out_cols:
                        if c not in df_enriched.columns:
                            df_enriched[c] = None
                    present_cols = out_cols  # insert in exact table order

                    con.register("df_batch", df_enriched[present_cols])
                    col_list = ", ".join(present_cols)
                    con.execute(f"INSERT INTO {out_table} ({col_list}) SELECT {col_list} FROM df_batch")
                finally:
                    con.close()

                written_total += len(df_enriched)
                self.logger.info(
                    f"[{table}] Sentiment batch {b+1}/{total_batches}: "
                    f"processed {len(df_enriched):,} rows, total written {written_total:,}/{rowcount:,}"
                )

            self.logger.info(f"Finished sentiment analysis for {table}: wrote {written_total:,} rows to '{out_table}'.")

    def _flatten(self) -> None:
        self.logger.info("Flattening Gedys objects")

        db = ETLDuckDBHandler(adapter=ETLAdapter.GEDYS)
        flattener = RecursiveJsonFlattener()
        batch_size = getattr(self.cfg.transform, "flatten_batch_size", 50_000)

        for table, model in self.cfg.extract.tables.items():
            if model.active is False:
                self.logger.info(f"Skipping inactive table: {table}")
                continue

            raw_table = f"{_safe_table_name(table)}_raw"
            sent_table = f"{_safe_table_name(table)}_sentiment"
            out_table = f"{_safe_table_name(table)}_flat"

            # Pick source: prefer curated sentiment table if it exists, else fall back to raw
            con = duckdb.connect(str(db.db_path))
            try:
                has_sent = bool(con.execute(
                    "SELECT 1 FROM duckdb_tables() WHERE table_name = ?", [sent_table]
                ).fetchone())
                src_table = sent_table if has_sent else raw_table

                exists_src = bool(con.execute(
                    "SELECT 1 FROM duckdb_tables() WHERE table_name = ?", [src_table]
                ).fetchone())
            finally:
                con.close()

            if not exists_src:
                self.logger.warning(f"No DuckDB table found for {table} (neither {sent_table} nor {raw_table}). Skipping.")
                continue

            # Row count
            con = duckdb.connect(str(db.db_path))
            try:
                rowcount = con.execute(f"SELECT COUNT(*) FROM {src_table}").fetchone()[0]
            finally:
                con.close()

            if rowcount == 0:
                self.logger.warning(f"No data in {src_table}. Skipping.")
                continue

            # Prepare empty output table (CREATE or REPLACE empty schema later from first batch)
            # We'll create the table on first non-empty flattened batch.
            created_out = False
            total_written = 0
            total_batches = math.ceil(rowcount / batch_size)
            select_sql = f"SELECT * FROM {src_table}"  # add ORDER BY <id> if you need deterministic order

            for b in range(total_batches):
                offset = b * batch_size
                con = duckdb.connect(str(db.db_path))
                try:
                    src_df = con.execute(f"{select_sql} LIMIT {batch_size} OFFSET {offset}").fetch_df()
                finally:
                    con.close()

                if src_df.empty:
                    continue

                # Flatten current batch (list[dict] -> list[dict])
                records = src_df.to_dict(orient="records")
                flat_records = flattener.flatten(records)  # keeps your existing recursive logic
                if not flat_records:
                    continue

                import pandas as pd
                flat_df = pd.DataFrame(flat_records)

                # Create output table on first batch using the DataFrame schema
                con = duckdb.connect(str(db.db_path))
                try:
                    if not created_out:
                        # Drop and create empty table with the incoming schema
                        con.execute(f"DROP TABLE IF EXISTS {out_table}")
                        con.register("df0", flat_df.head(0))
                        con.execute(f"CREATE TABLE {out_table} AS SELECT * FROM df0")
                        created_out = True
                    else:
                        # Schema evolution: add any new columns (as VARCHAR) that appear later
                        out_cols = {r[0] for r in con.execute(f"DESCRIBE {out_table}").fetchall()}
                        new_cols = [c for c in flat_df.columns if c not in out_cols]
                        for c in new_cols:
                            # Using quoted identifier to allow dots or special chars in column names
                            con.execute(f'ALTER TABLE {out_table} ADD COLUMN "{c}" VARCHAR')
                    # Align columns: ensure all out_table columns exist in df; add missing with None
                    out_cols_ordered = [r[0] for r in con.execute(f"DESCRIBE {out_table}").fetchall()]
                    for c in out_cols_ordered:
                        if c not in flat_df.columns:
                            flat_df[c] = None
                    # Insert in exact table column order
                    con.register("df_batch", flat_df[out_cols_ordered])
                    col_list = ", ".join(f'"{c}"' for c in out_cols_ordered)
                    con.execute(f"INSERT INTO {out_table} ({col_list}) SELECT {col_list} FROM df_batch")
                finally:
                    con.close()

                total_written += len(flat_df)
                self.logger.info(
                    f"[{table}] Flatten batch {b+1}/{total_batches}: "
                    f"processed {len(flat_df):,} rows, total written {total_written:,}/{rowcount:,}"
                )

            if not created_out:
                self.logger.warning(f"No flattened rows produced for {table} (source {src_table}).")
            else:
                self.logger.info(
                    f"Finished flattening for {table}: wrote {total_written:,} rows to '{out_table}'."
                )

    def _join(self) -> None:
        self.logger.info("Joining Gedys objects")

        db = ETLDuckDBHandler(adapter=ETLAdapter.GEDYS)

        # We expect three flattened tables
        company_flat = f"{_safe_table_name('Company')}_flat"
        contact_flat = f"{_safe_table_name('Contact')}_flat"
        opp_flat     = f"{_safe_table_name('Opportunity')}_flat"

        out_table = _safe_table_name("Company Joined")  # target table name: company_joined

        # Check required sources
        con = duckdb.connect(str(db.db_path))
        try:
            def _exists(table_name: str) -> bool:
                return bool(con.execute(
                    "SELECT 1 FROM duckdb_tables() WHERE table_name = ?", [table_name]
                ).fetchone())

            has_company = _exists(company_flat)
            has_contact = _exists(contact_flat)
            has_opp     = _exists(opp_flat)

        finally:
            con.close()

        if not has_company:
            raise ValueError(f"No company data found in DuckDB (expected table {company_flat}).")
        if not has_contact:
            raise ValueError(f"No contact data found in DuckDB (expected table {contact_flat}).")
        if not has_opp:
            self.logger.warning(f"No opportunity data found in DuckDB (expected table {opp_flat}). Proceeding with company-contact join only.")

        # Build SQL with defensive quoting for dotted column names
        # Assumptions:
        # - Company key column: "Oid"
        # - Contact key column: "Oid"
        # - Opportunity relationship columns: "RelatedMainParents.Oid", "RelatedParents.Oid"
        # Adjust if your column names differ after flattening.
        join_sql = f"""
            CREATE OR REPLACE TABLE {out_table} AS
            SELECT
                c.*,
                ct.*,
                op.*
            FROM {company_flat} AS c
            LEFT JOIN {contact_flat} AS ct
                ON (ct."RelatedMainParents.Oid" = c."Oid" OR ct."RelatedParents.Oid" = c."Oid")
            LEFT JOIN {opp_flat} AS op
                ON (
                    op."RelatedMainParents.Oid" = c."Oid" OR
                    op."RelatedParents.Oid"     = c."Oid" OR
                    op."RelatedMainParents.Oid" = ct."Oid" OR
                    op."RelatedParents.Oid"     = ct."Oid"
                )
        """

        # Execute join; if opportunities table is missing, join only company-contact
        if not has_opp:
            join_sql = f"""
                CREATE OR REPLACE TABLE {out_table} AS
                SELECT
                    c.*,
                    ct.*
                FROM {company_flat} AS c
                LEFT JOIN {contact_flat} AS ct
                    ON (ct."RelatedMainParents.Oid" = c."Oid" OR ct."RelatedParents.Oid" = c."Oid")
            """

        con = duckdb.connect(str(db.db_path))
        try:
            con.execute(join_sql)
            # Optional: count rows for logging
            cnt = con.execute(f"SELECT COUNT(*) FROM {out_table}").fetchone()[0]
        finally:
            con.close()

        self.logger.info(f"Finished joining into '{out_table}'. Row count: {cnt:,}")