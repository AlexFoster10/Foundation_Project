import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/processing.log', filemode='w')

def daily_return(df):
    try:
        df['daily_return'] = (df['close'] - df['open']) / df['open']
        return df
    except Exception as e:
        logging.error(f"Error calculating daily return: {e}")
        df['daily_return'] = np.nan
        return df
    
def price_spread(df):
    try:
        df['price_spread'] = df['high'] - df['low']
        return df
    except Exception as e:
        logging.error(f"Error calculating price spread: {e}")
        df['price_spread'] = np.nan
        return df


##not finished yet dont fully understand SMA
def simple_moving_average(df, window):
    try:
        df['simple_moving_average'] = df['close'].rolling(window=window).mean()
        return df
    except Exception as e:
        logging.error(f"Error calculating simple moving average: {e}")
        df['simple_moving_average'] = np.nan
        return df
    
def volume_change(df):
    try:
        groups = df.groupby('ticker')
        df['volume_change'] = groups['volume'].pct_change()
        return df
    except Exception as e:
        logging.error(f"Error calculating volume change: {e}")
        df['volume_change'] = np.nan
        return df
