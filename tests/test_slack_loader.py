import unittest
import pandas as pd
from src.loader import SlackDataLoader

class TestSlackLoader(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or configurations
        pass

    def test_load_data(self):
        # Test the basic functionality of loading data
        loader = SlackDataLoader()  # Adjust based on your actual implementation
        dataframe = loader.load_data()
        self.assertIsInstance(dataframe, pd.DataFrame, "Data is not loaded as a DataFrame")

    def test_expected_columns(self):
        # Test that the SlackDataLoader returns a DataFrame with the expected columns
        loader = SlackDataLoader()  # Adjust based on your actual implementation
        dataframe = loader.load_data()
        expected_columns = ['user', 'timestamp', 'message', 'channel']  # Adjust based on your actual columns
        actual_columns = dataframe.columns.tolist()
        self.assertEqual(expected_columns, actual_columns, "Columns do not match expected")

    def test_data_types(self):
        # Test that the data types of the columns are as expected
        loader = SlackDataLoader()  # Adjust based on your actual implementation
        dataframe = loader.load_data()
        expected_data_types = {'user': str, 'timestamp': pd.Timestamp, 'message': str, 'channel': str}
        actual_data_types = dataframe.dtypes.to_dict()
        for column, expected_type in expected_data_types.items():
            self.assertEqual(expected_type, actual_data_types[column], f"Data type for {column} does not match expected")

    def test_data_not_empty(self):
        # Test that the loaded data is not empty
        loader = SlackDataLoader()  # Adjust based on your actual implementation
        dataframe = loader.load_data()
        self.assertFalse(dataframe.empty, "Loaded DataFrame is empty")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
