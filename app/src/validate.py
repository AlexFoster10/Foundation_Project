import pandas as pd
from . import  logging_config
from  .logging_config import main_logger
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_path = os.path.join(BASE_DIR, "app", "tests", "logs", "validate.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)


logger =  logging_config.setup_logger('validate_logger', log_path)


def clean_df(df):
    numericized = False
    df_orig = df
    #drop all na values from the dataframe, if any
    try:
        
        df = df.dropna()
        main_logger.info("Successfully dropped NA values from DataFrame")
    except Exception as e:
        logger.info(f"na values could not be removed from DataFrame: {e}")
        main_logger.info(f"na values could not be removed from DataFrame: {e}")

    #drop all rows where data is not numeric, i.e. where high, low, open or close is not a number
    try:
        df.loc[:, 'high'] = pd.to_numeric(df['high'], errors='coerce')
        df.loc[:, 'low'] = pd.to_numeric(df['low'], errors='coerce')
        df.loc[:, 'open'] = pd.to_numeric(df['open'], errors='coerce')
        df.loc[:, 'close'] = pd.to_numeric(df['close'], errors='coerce')
        df.loc[:, 'volume'] = pd.to_numeric(df['volume'], errors='coerce')
        df = df.dropna(subset=['high', 'low', 'open', 'close', 'volume'])
        numericized = True

        main_logger.info("Successfully converted high, low, open, close and volume columns to numeric values")

    except Exception as e:
        logger.info(f"Non-numeric values could not be removed from DataFrame: {e}")
        main_logger.info(f"Non-numeric values could not be removed from DataFrame: {e}")


    #drop all rows where logic doesn't work, i.e. where high is less than low
    if numericized:
        df = df[df['high'] >= df['low']]
        df = df[df['high'] >= df['open']]
        df = df[df['high'] >= df['close']]
        df = df[df['high'] > 0]
        df = df[df['low'] <= df['open']]
        df = df[df['low'] <= df['close']]
        df = df[df['low'] > 0]
        df = df[df['open'] > 0]
        df = df[df['close'] > 0]
        df = df[df['volume'] > 0]


    #drop rows where date time format is not correct
    try:
        df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y-%m-%d', errors='coerce')
        df = df.dropna(subset=['trade_date'])
        main_logger.info("Successfully converted trade_date column to datetime format and dropped invalid dates")
    except Exception as e:
        logger.info(f"Invalid date format could not be removed from DataFrame: {e}")
        main_logger.info(f"Invalid date format could not be removed from DataFrame: {e}")

    #log dropped rows
    dropped_rows = df_orig[~df_orig.index.isin(df.index)]
    logger.info(f"Dropped rows due to invalid data:\n{dropped_rows}")
    main_logger.info(f"Dropped rows due to invalid data:\n{dropped_rows}")

    df = df.sort_values(by=['ticker', 'trade_date'])

    return df
        

    


