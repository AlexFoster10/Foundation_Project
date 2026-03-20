import pathlib
import sys
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)

import unittest
from app.src import output
import pandas as pd

class TestOutput(unittest.TestCase):
    
    def test_output_csv(self):
        # Create a sample DataFrame
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)

        # Test output_csv function
        output.output_csv(df, "app/tests/test_data/test_output.csv")
        # Read the output file and check if it matches the original DataFrame
        output_df = pd.read_csv("app/tests/test_data/test_output.csv")
        print(df)
        print(output_df)
        pd.testing.assert_frame_equal(df, output_df)


    

if __name__ == '__main__':
    unittest.main() 