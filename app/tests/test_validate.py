import pathlib
import sys
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

import unittest
from app.src import validate
import pandas as pd

# Load the test data
test_clean_df = pd.read_csv("app/tests/test_data/clean_test_data.csv")
test_clean_df["trade_date"] = pd.to_datetime(test_clean_df["trade_date"])

test_dirty_df = pd.read_csv("app/tests/test_data/dirty_test_data.csv")

class TestValidate(unittest.TestCase):

    # Test clean_df function
    def test_clean_df(self):
        result_df = validate.clean_df(test_dirty_df)
        pd.testing.assert_frame_equal(result_df,test_clean_df)

        


if __name__ == '__main__':
    unittest.main()