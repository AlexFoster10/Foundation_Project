import validate, ingest
import pandas as pd


def main():
    df = ingest.ingest_csv("./data/raw/marketData.csv")
    df = validate.clean_df(df)


if __name__ == "__main__":
    main()