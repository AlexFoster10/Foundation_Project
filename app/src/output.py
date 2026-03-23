import pandas as pd
import logging
from  .logging_config import main_logger
from . import  logging_config
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


logger =  logging_config.setup_logger('output_logger', 'app/tests/logs/output.log')
def output_csv(df, path="placeholder"):

    if path == "placeholder":
        path = input("Enter the path to save the output CSV file (default: app/data/processed/processed_data.csv): ")

    try:
        df.to_csv(path, index=False)
        logger.info(f"Successfully output CSV file: {path}")
        main_logger.info(f"Successfully output CSV file: {path}")
    except Exception as e:
        logger.error(f"Error outputting CSV file, default destination used: {e}")
        main_logger.error(f"Error outputting CSV file, default destination used: {e}")
        df.to_csv(config['default_csv_path_out'], index=False)



