import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/validate.log', filemode='w')
   

def clean_df(df):

    numericized = False
    df_orig = df.copy()
    #drop all na values from the dataframe, if any
    try:
        
        df = df.dropna()
    except Exception as e:
        logging.info(f"na values could not be removed from DataFrame: {e}")

    #drop all rows where data is not numeric, i.e. where high, low, open or close is not a number
    try:
        df['high'] = pd.to_numeric(df['high'], errors='coerce')
        df['low'] = pd.to_numeric(df['low'], errors='coerce')
        df['open'] = pd.to_numeric(df['open'], errors='coerce')
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
        df = df.dropna(subset=['high', 'low', 'open', 'close', 'volume'])
        numericized = True

    except Exception as e:
        logging.info(f"Non-numeric values could not be removed from DataFrame: {e}")


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


    #drop rows where date time format is not correct
    try:
        df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y-%m-%d', errors='coerce')
        df = df.dropna(subset=['trade_date'])
    except Exception as e:
        logging.info(f"Invalid date format could not be removed from DataFrame: {e}")

    #log dropped rows
    dropped_rows = df_orig[~df_orig.index.isin(df.index)]
    logging.info(f"Dropped rows due to invalid data:\n{dropped_rows}")

    print(df)

    return df
        

    


