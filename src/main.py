import validate


def main():
    validate.validate_csv("./data/raw/marketData.csv")
    validate.clean_df("./data/raw/marketData.csv")


if __name__ == "__main__":
    main()