# Import necessary library
import pandas as pd

# File paths
grades_file = "grades.csv"
weights_file = "weights.csv"
results_file = 'result.csv'

# Load both files into DataFrames
grades_df = pd.read_csv(grades_file, dtype=str).fillna('')
weights_df = pd.read_csv(weights_file, dtype=str).fillna('')

# Ensure both dataframes have consistent column order
if set(grades_df.columns) == set(weights_df.columns):
    # Convert to numerical values for calculation, replacing empty strings with zero
    grades_numeric = grades_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)
    weights_numeric = weights_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Calculate the product rounded as specified
    total_grades = ((grades_numeric * weights_numeric) / 100).sum(axis=1).round()

    # Insert course names back
    result_df = pd.DataFrame({
        "course number": range(1, len(total_grades) + 1),
        "course name": grades_df["course"],
        "grade": total_grades
    })
    filtered_grades = result_df[result_df["grade"] > 59]
    result_df.to_csv(results_file)

    average_filtered_grade = filtered_grades["grade"].mean()
    print("Your Average is: {}".format(average_filtered_grade))
else:
    raise ValueError("The columns in the grades and weights files do not match.")

