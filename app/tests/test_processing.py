import pathlib
import sys
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

import unittest
from app.src import processing
import pandas as pd



df = pd.read_csv("app/tests/test_data/clean_test_data_large.csv")

class TestProcessing(unittest.TestCase):

    # Test daily_return function
    def test_daily_return(self):
        result_df = processing.daily_return(df)

        # Test each row comparing the calculated daily return with the expected value
        for index, row in df.iterrows():
            expected_return = (row['close'] - row['open']) / row['open']
            self.assertAlmostEqual(result_df.loc[index, 'daily_return'], expected_return)

    # Test price_spread function
    def test_price_spread(self):
        result_df = processing.price_spread(df)

        # Test each row comparing the calculated price spread with the expected value
        for index, row in df.iterrows():
            expected_spread = row['high'] - row['low']
            self.assertAlmostEqual(result_df.loc[index, 'price_spread'], expected_spread)

    # Test volume_change function
    def test_volume_change(self):
        result_df = processing.volume_change(df)

        # Test each row comparing the calculated volume change with the expected value 
        # The first row and rows where the ticker changes should have NaN for volume change
        for index, row in df.iterrows():
            if index == 0:
                expected_change = None
            elif row['ticker'] != df.loc[index - 1, 'ticker']:
                expected_change = None
            else:
                expected_change = (row['volume'] - df.loc[index - 1, 'volume']) / df.loc[index - 1, 'volume']
            if expected_change is None:
                self.assertTrue(pd.isna(result_df.loc[index, 'volume_change']))
            else:
                self.assertAlmostEqual(result_df.loc[index, 'volume_change'], expected_change)

        
if __name__ == '__main__':
    unittest.main() 