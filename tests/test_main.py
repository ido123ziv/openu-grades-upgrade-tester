import pandas as pd


def test_dataframe_shapes(sample_dataframes):
    grades_df, weights_df = sample_dataframes
    assert grades_df.shape[0] == weights_df.shape[0], "Both DataFrames should have the same number of rows"
    assert pd.notna(grades_df.iloc[1]['exam']), "Can't use empty exams"


# 1. Test data processing
def test_process_grades(sample_dataframes):
    processed_grades, processed_weights = sample_dataframes
    assert processed_grades.shape == (3, 4), "Processed grades should have the correct dimensions"
    assert processed_weights.iloc[1]['exam'] > processed_weights.iloc[1]['mmn1'], "Weight should be correctly assigned"


# # 2. Test total grades calculation
# def test_calculate_total_grades():
#     total_grades = calculate_total_grades(process_grades(grades_sample, weights_sample))
#     assert total_grades[0] == 92.5, "Total grade for Course1 should be 92.5"
#     assert total_grades[1] < 60, "Course2 should have a grade below 60"
#
#
# # 3. Test filtering logic
# def test_filter_grades():
#     total_grades = pd.Series([92.5, 50, 77.5])
#     filtered_grades = filter_grades(total_grades)
#     assert len(filtered_grades) == 2, "Only grades >= 60 should be included"
#     assert filtered_grades.iloc[0] == 92.5, "First course should be Course1 with a grade of 92.5"
