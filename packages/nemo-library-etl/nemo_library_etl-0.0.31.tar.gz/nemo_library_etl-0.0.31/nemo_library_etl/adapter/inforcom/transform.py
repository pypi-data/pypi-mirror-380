"""
InforCOM ETL Transform Module.

This module handles the transformation phase of the InforCOM ETL pipeline.
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
    InforCOMTransform: Main class handling InforCOM data transformation.
"""

from prefect import get_run_logger
from nemo_library_etl.adapter.inforcom.config_models import PipelineInforCOM
from nemo_library_etl.adapter._utils.enums import ETLAdapter, ETLStep
from nemo_library_etl.adapter._utils.file_handler import ETLFileHandler
from nemo_library import NemoLibrary
import pandas as pd


class InforCOMTransform:
    """
    Handles transformation of extracted InforCOM data.

    This class manages the transformation phase of the InforCOM ETL pipeline,
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
        cfg (PipelineInforCOM): Pipeline configuration with transformation settings.
    """

    def __init__(self, cfg: PipelineInforCOM):
        """
        Initialize the InforCOMTransform instance.

        Sets up the transformer with the necessary library instances, configuration,
        and logging capabilities for the transformation process.

        Args:
            cfg (PipelineInforCOM): Pipeline configuration object containing
                                                          transformation settings and rules.
        """
        self.nl = NemoLibrary()
        self.config = self.nl.config
        self.logger = get_run_logger()
        self.cfg = cfg

        super().__init__()

    def transform(self) -> None:
        """
        Execute the main transformation process for InforCOM data.

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
            the specific InforCOM system requirements and business rules.
        """
        self.logger.info("Transforming all InforCOM objects")

        # transform objects
        self.beauftify()

    def beauftify(self) -> None:
        """
        Beautify the transformed InforCOM data.

        This method applies final formatting and structuring to the transformed data
        to ensure it meets the required standards for loading into the target system.

        The beautification process may include:
        - Standardizing column names and data formats
        - Removing unnecessary whitespace or special characters
        - Ensuring consistent data types across records
        - Applying any final business rules or adjustments

        The method provides logging for tracking the beautification process.

        Note:
            The actual beautification logic needs to be implemented based on
            the specific InforCOM system requirements and target system standards.
        """
        self.logger.info("Beautifying all InforCOM objects")

        fh = ETLFileHandler()
        # beautify objects
        for table, model in self.cfg.extract.tables.items():
            if model.active is False:
                self.logger.info(f"Skipping inactive table: {table}")
                continue

            self.logger.info(f"Beautifying table: {table}")
            data = fh.readJSONL(
                adapter=ETLAdapter.INFORCOM,
                step=ETLStep.EXTRACT,
                entity=table,
            )
            if data is None:
                self.logger.warning(f"No data found for table: {table}")
                continue

            df = pd.DataFrame(data)
            self.logger.info(f"Initial data shape for {table}: {df.shape}")