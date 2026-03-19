import unittest
from app.src import ingest
import pandas as pd

class TestIngest(unittest.TestCase):

    def test_ingest_csv(self):
        # Test with a valid file path
        df = ingest.ingest_csv("app/data/raw/marketData2.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

        # Test with an invalid file path
        df = ingest.ingest_csv("app/data/raw/nonexistent.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)