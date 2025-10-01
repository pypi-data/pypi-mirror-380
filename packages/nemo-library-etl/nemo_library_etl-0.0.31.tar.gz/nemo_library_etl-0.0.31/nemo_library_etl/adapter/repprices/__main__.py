"""
RepPrices ETL Adapter Main Entry Point.

This module serves as the main entry point for the RepPrices ETL adapter, which handles
the extraction, transformation, and loading of data from RepPrices systems into Nemo.
"""
from nemo_library_etl.adapter.repprices.flow import repprices_flow

def main() -> None:
    """
    Main function to execute the RepPrices ETL flow.

    This function initiates the complete RepPrices ETL process by calling the RepPrices_flow
    function, which orchestrates the extract, transform, and load operations.
    """
    repprices_flow()


if __name__ == "__main__":
    main()
