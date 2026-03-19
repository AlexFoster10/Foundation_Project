import pandas as pd
import logging
import numpy as np
import logging_config
from logging_config import main_logger
logger = logging_config.setup_logger('processing_logger', './tests/logs/processing.log')


def daily_return(df):
    try:
        df['daily_return'] = (df['close'] - df['open']) / df['open']
        main_logger.info("Successfully calculated daily return")
        return df
    except Exception as e:
        logger.error(f"Error calculating daily return: {e}")
        #main_logger.error(f"Error calculating daily return: {e}")
        df['daily_return'] = np.nan
        return df
    
def price_spread(df):
    try:
        df['price_spread'] = df['high'] - df['low']
        main_logger.info("Successfully calculated price spread")
        return df
    except Exception as e:
        logger.error(f"Error calculating price spread: {e}")
        #main_logger.error(f"Error calculating price spread: {e}")
        df['price_spread'] = np.nan
        return df


##not finished yet dont fully understand SMA
def simple_moving_average(df, window):
    try:
        df['simple_moving_average'] = df['close'].rolling(window=window).mean()
        return df
    except Exception as e:
        logger.error(f"Error calculating simple moving average: {e}")
        #main_logger.error(f"Error calculating simple moving average: {e}")
        df['simple_moving_average'] = np.nan
        return df
    
def volume_change(df):
    try:
        groups = df.groupby('ticker')
        df['volume_change'] = groups['volume'].pct_change()
        main_logger.info("Successfully calculated volume change")
        return df
    except Exception as e:
        logger.error(f"Error calculating volume change: {e}")
        #main_logger.error(f"Error calculating volume change: {e}")
        df['volume_change'] = np.nan
        return df
