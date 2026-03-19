import pandas as pd
from . import  logging_config
from  .logging_config import main_logger

logger =  logging_config.setup_logger('ingest_logger', 'app/tests/logs/ingest.log')

def ingest_csv(path="app/data/raw/marketData2.csv"):

    if not path:
        path = input("Enter the path to the CSV file to ingest (default: app/data/raw/marketData2.csv): ")
    try:
        df = pd.read_csv(path)
        main_logger.info(f"Successfully ingested CSV file: {path}")
        return df
    except Exception as e:
        logger.error(f"Error ingesting CSV file, default used: {e}")
        main_logger.error(f"Error ingesting CSV file, default used: {e}")
        #generate a default dataframe with the correct columns and return it
        df = pd.read_csv("app/data/raw/marketData.csv")
        return df
    