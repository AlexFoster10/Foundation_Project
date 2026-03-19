import validate, ingest, processing, output
import pandas as pd


def main():
    df = ingest.ingest_csv("./data/raw/marketData2.csv")
    df = validate.clean_df(df)
    df = processing.daily_return(df)
    df = processing.price_spread(df)
    #df = processing.simple_moving_average(df,5)
    df = processing.volume_change(df)
    output.output_csv(df)


if __name__ == "__main__":
    main()