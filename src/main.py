import validate


def main():
    validate.validate_csv("./data/marketData.csv")
    validate.clean_df("./data/marketData.csv")


if __name__ == "__main__":
    main()