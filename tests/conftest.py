import pytest
import pandas as pd


@pytest.fixture
def sample_dataframes():
    # Replace with your own test paths or keep these for demonstration
    grades_file = 'data/test_grades.csv'
    weights_file = 'data/test_weights.csv'

    # Read the CSVs into DataFrames
    grades_df = pd.read_csv(grades_file)
    weights_df = pd.read_csv(weights_file)

    # Return the DataFrames as a tuple for test functions to use
    return grades_df, weights_df
