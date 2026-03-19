import pandas as pd
import logging
from logging_config import main_logger
import logging_config


logger = logging_config.setup_logger('output_logger', './tests/logs/output.log')
def output_csv(df, path="./data/processed/processed_data.csv"):

    if not path:
        path = input("Enter the path to save the output CSV file (default: ./data/processed/processed_data.csv): ")

    try:
        df.to_csv(path)
    except Exception as e:
        logger.error(f"Error outputting CSV file: {e}")
        main_logger.error(f"Error outputting CSV file: {e}")



