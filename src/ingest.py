import pandas as pd
import logging
import logging_config
from logging_config import main_logger


logger = logging_config.setup_logger('output_logger', './tests/logs/ingest.log')

def ingest_csv(path="./data/raw/marketData2.csv"):

    if not path:
        path = input("Enter the path to the CSV file to ingest (default: ./data/raw/marketData2.csv): ")
    try:
        df = pd.read_csv(path)
        main_logger.info(f"Successfully ingested CSV file: {path}")
        return df
    except Exception as e:
        logger.error(f"Error ingesting CSV file, defualt generated: {e}")
        main_logger.error(f"Error ingesting CSV file, defualt generated: {e}")
        #generate a default dataframe with the correct columns and return it
        df = pd.DataFrame(columns=['ticker', 'trade_date', 'open', 'high', 'low', 'close', 'volume'])
        return df
    