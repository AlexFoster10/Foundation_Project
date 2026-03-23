import pathlib
import sys
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

from app.src import validate,  ingest,  processing,  output, database
import pandas as pd
import logging
import matplotlib.pyplot as plt

# Set up logging
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

    # Ingest, validate, process, and output data
    df =  ingest.ingest_csv("app/data/raw/marketData2.csv")
    df =  validate.clean_df(df)
    pf = df.copy()
    df =  processing.daily_return(df)
    df =  processing.price_spread(df)
    df = processing.simple_moving_average(df,3)
    df =  processing.volume_change(df)
    output.output_csv(df,"app/data/processed/processed_data.csv")


    # Plotting graph
    for ticker, group in df.groupby("ticker"):
        group = group.sort_values("trade_date")
        plt.plot(group["trade_date"], group["close"], label=ticker)
    plt.legend(title="Ticker")
    plt.title("Stock Prices by Ticker")
    plt.ylabel("Close Price")
    plt.xticks(rotation=20)
    plt.savefig("app/data/plots/processed_data.png")

    database.create_new_table(df)



if __name__ == "__main__":
    main()