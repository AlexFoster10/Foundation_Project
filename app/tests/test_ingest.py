import pathlib
import sys
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

import unittest
from app.src import ingest
import pandas as pd

class TestIngest(unittest.TestCase):

    def test_valid_path(self):
        # Test with a valid file path
        df = ingest.ingest_csv("app/data/raw/marketData2.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_invalid_path(self):
        # Test with an invalid file path
        df = ingest.ingest_csv("app/data/raw/nonexistent.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()