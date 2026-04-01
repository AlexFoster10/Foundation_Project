import pathlib
import sys

from fastapi.responses import HTMLResponse
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

from app.src import validate,  ingest,  processing,  output, database
import pandas as pd
import logging
import matplotlib.pyplot as plt
from fastapi import FastAPI
import yaml

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

    # Allow user to specify input path as command line argument, if not provided use default path
    if len(sys.argv) > 1:
        df =  ingest.ingest_csv(sys.argv[1])
    else:
        df =  ingest.ingest_csv()

    # Fully process the data and add new columns for each processing step, if there is an error in any step log the error and continue with the next steps, filling in any missing values with NaN
    df =  validate.clean_df(df)
    df =  processing.daily_return(df)
    df =  processing.price_spread(df)
    df = processing.simple_moving_average(df,3)
    df =  processing.volume_change(df)

    # Allow user to specify output path as command line argument, if not provided use default path
    if len(sys.argv) > 2:
        output.output_csv(df, sys.argv[2])
    else:
        output.output_csv(df)


    # Plotting graph
    for ticker, group in df.groupby("ticker"):
        group = group.sort_values("trade_date")
        plt.plot(group["trade_date"], group["close"], label=ticker)
    plt.legend(title="Ticker")
    plt.title("Stock Prices by Ticker")
    plt.ylabel("Close Price")
    plt.xticks(rotation=20)
    plt.savefig("app/data/plots/processed_data.png")

    # Save to database
    database.append_to_table(df)



if __name__ == "__main__":
    main()




app = FastAPI()

# Endpoint to display the processed data as an HTML table
@app.get("/")
async def root(response_class=HTMLResponse):
    df = ingest.ingest_csv("app/data/processed/processed_data.csv")
    html = df.to_html()
    return HTMLResponse(content=html, status_code=200)
