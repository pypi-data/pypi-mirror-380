"""
RepPrices ETL Flow Module.

This module defines the Prefect workflow for the RepPrices ETL process. It orchestrates
the extraction, transformation, and loading of data from RepPrices systems into Nemo
using Prefect tasks and flows for robust pipeline execution.

The flow consists of three main phases:
1. Extract: Retrieve data from RepPrices system
2. Transform: Process and clean the extracted data
3. Load: Insert the transformed data into Nemo

Each phase can be individually enabled/disabled through configuration settings.
"""

import logging
from typing import Union
from prefect import flow, task, get_run_logger
from nemo_library_etl.adapter.repprices.config_models import PipelineRepPrices
from nemo_library_etl.adapter._utils.config import load_pipeline_config
from nemo_library_etl.adapter.repprices.extract import RepPricesExtract
from nemo_library_etl.adapter.repprices.transform import RepPricesTransform
from nemo_library_etl.adapter.repprices.load import RepPricesLoad


@flow(name="RepPrices ETL Flow", log_prints=True)
def repprices_flow() -> None:
    """
    Main Prefect flow for the RepPrices ETL pipeline.

    This flow orchestrates the complete ETL process for RepPrices data, including:
    - Loading pipeline configuration from JSON files
    - Conditionally executing extract, transform, and load phases based on configuration
    - Comprehensive logging and error handling throughout the process
    - Integration with Prefect for workflow orchestration, monitoring, and retry logic
    
    The flow follows a sequential execution pattern where each phase (extract, transform, load)
    is executed as a separate Prefect task. Each phase can be individually enabled or disabled
    through the pipeline configuration settings.
    
    Pipeline Configuration:
        The flow loads its configuration using the load_pipeline_config utility, which reads
        settings from JSON configuration files. The configuration includes:
        - Extract settings: table specifications and activation flags
        - Transform settings: business rules and data processing parameters  
        - Load settings: target system configuration and batch parameters
        - Global settings: phase activation flags (extract_active, transform_active, load_active)
    
    Error Handling:
        Any exceptions raised during the ETL process will be logged and propagated by Prefect,
        enabling built-in retry mechanisms and failure notifications.
    
    Returns:
        None
        
    Raises:
        Exception: Any exception raised during the ETL process will be logged
                  and propagated by Prefect for proper error handling and monitoring.
    """    
    logger = get_run_logger()
    logger.info("Starting RepPrices ETL Flow")

    # load config
    cfg = load_pipeline_config("RepPrices")

    # run steps
    if cfg.extract_active:
        logger.info("Extracting objects from RepPrices")
        extract(cfg=cfg,logger=logger)

    if cfg.transform_active:
        logger.info("Transforming RepPrices objects")
        transform(cfg=cfg,logger=logger)

    if cfg.load_active:
        logger.info("Loading RepPrices objects")
        load(cfg=cfg,logger=logger)

    logger.info("RepPrices ETL Flow finished")


@task(name="Extract All Objects from RepPrices")
def extract(cfg: PipelineRepPrices, logger: Union[logging.Logger, object]) -> None:
    """
    Prefect task to extract data from RepPrices system.

    This task handles the extraction phase of the ETL pipeline, retrieving
    data from the RepPrices system based on the configuration settings.
    It manages table-specific extraction settings and respects activation flags.
    
    Args:
        cfg (PipelineRepPrices): Pipeline configuration containing extraction settings,
                                                      including table configurations and activation flags.
        logger (Union[logging.Logger, object]): Logger instance for recording execution details.
                                               Can be a standard Python logger or Prefect logger.
    
    Returns:
        None
        
    Note:
        The actual extraction logic is delegated to the RepPricesExtract class.
    """
    logger.info("Extracting all RepPrices objects")
    extractor = RepPricesExtract(cfg=cfg)
    extractor.extract()


@task(name="Transform Objects")
def transform(cfg: PipelineRepPrices, logger: Union[logging.Logger, object]) -> None:
    """
    Prefect task to transform extracted RepPrices data.

    This task handles the transformation phase of the ETL pipeline, processing
    and cleaning the extracted data to prepare it for loading into Nemo.
    It applies business rules, data validation, and formatting operations.
    
    Args:
        cfg (PipelineRepPrices): Pipeline configuration containing transformation settings,
                                                      including business rules and data processing parameters.
        logger (Union[logging.Logger, object]): Logger instance for recording execution details.
                                               Can be a standard Python logger or Prefect logger.
    
    Returns:
        None
        
    Note:
        The actual transformation logic is delegated to the RepPricesTransform class.
    """
    logger.info("Transforming RepPrices objects")
    transformer = RepPricesTransform(cfg=cfg)
    transformer.transform()

@task(name="Load Objects")
def load(cfg: PipelineRepPrices, logger: Union[logging.Logger, object]) -> None:
    """
    Prefect task to load transformed data into target system.
    
    This task handles the loading phase of the ETL pipeline, inserting
    the transformed data into the target system with proper error handling
    and performance optimization.

    Args:
        cfg (PipelineRepPrices): Pipeline configuration containing load settings,
                                                      including target system configuration and batch parameters.
        logger (Union[logging.Logger, object]): Logger instance for recording execution details.
                                               Can be a standard Python logger or Prefect logger.
    
    Returns:
        None
        
    Note:
        The actual loading logic is delegated to the RepPricesLoad class.
    """
    logger.info("Loading RepPrices objects into target system")
    loader = RepPricesLoad(cfg=cfg)
    loader.load()

