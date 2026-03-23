import pandas as pd
from . import  logging_config
from  .logging_config import main_logger
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

logger =  logging_config.setup_logger('ingest_logger', 'app/tests/logs/ingest.log')

def ingest_csv(path="placeholder"):

    if path == "placeholder":
        path = input("Enter the path to the CSV file to ingest (default: app/data/raw/marketData2.csv): ")
    try:
        df = pd.read_csv(path)
        logger.info(f"Successfully ingested CSV file: {path}")
        main_logger.info(f"Successfully ingested CSV file: {path}")
        return df
    except Exception as e:
        logger.error(f"Error ingesting CSV file, default used: {e}")
        main_logger.error(f"Error ingesting CSV file, default used: {e}")
        #generate a default dataframe with the correct columns and return it
        df = pd.read_csv(config['default_csv_path_in'])
        return df
    