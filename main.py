# Import necessary library
import pandas as pd

# File paths
grades_file = "/mnt/data/grades.csv"
weights_file = "/mnt/data/weights.csv"

# Load both files into DataFrames
grades_df = pd.read_csv(grades_file, dtype=str).fillna('')
weights_df = pd.read_csv(weights_file, dtype=str).fillna('')

# Ensure both dataframes have consistent column order
if set(grades_df.columns) == set(weights_df.columns):
    # Convert to numerical values for calculation, replacing empty strings with zero
    grades_numeric = grades_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)
    weights_numeric = weights_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Calculate the product rounded as specified
    weighted_products = ((grades_numeric * weights_numeric) / 100).round()

    # Insert course names back
    weighted_products.insert(0, "course", grades_df["course"])

    # Display the calculated products
    import ace_tools as tools;

    tools.display_dataframe_to_user("Calculated Weighted Products", weighted_products)
else:
    raise ValueError("The columns in the grades and weights files do not match.")
