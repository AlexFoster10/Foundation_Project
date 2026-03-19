import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/output.log', filemode='w')   

def output_csv(df):
    try:
        df.to_csv('./data/processed/processed_data.csv')
    except Exception as e:
        logging.error(f"Error outputting CSV file: {e}")