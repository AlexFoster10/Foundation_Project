from app.src import validate,  ingest,  processing,  output
import pandas as pd
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file, mode="w")      
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

main_logger = setup_logger('main_logger', 'app/tests/logs/main.log')


def main():
    df =  ingest.ingest_csv("app/data/raw/marketData2.csv")
    df =  validate.clean_df(df)
    df =  processing.daily_return(df)
    df =  processing.price_spread(df)
    #df = processing.simple_moving_average(df,5)
    df =  processing.volume_change(df)
    output.output_csv(df,"app/data/processed/processed_data.csv")


if __name__ == "__main__":
    main()