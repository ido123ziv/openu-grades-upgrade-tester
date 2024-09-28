import pandas as pd
import numpy as np

# File paths
grades_file = "data/grades.csv"
weights_file = "data/weights.csv"
current_results_file = 'outputs/result.csv'
improved_results_file = 'outputs/improved_result.csv'

# Load both files into DataFrames
basic_grades_df = pd.read_csv(grades_file, dtype=str).fillna('')
basic_weights_df = pd.read_csv(weights_file, dtype=str).fillna('')


def get_current_average(grades_df: pd.DataFrame, weights_df: pd.DataFrame, debug=False):
    cgrades_df = grades_df.copy()
    cweights_df = weights_df.copy()
    # Ensure both dataframes have consistent column order
    if set(cgrades_df.columns) == set(cweights_df.columns):
        # Convert to numerical values for calculation, replacing empty strings with zero
        grades_numeric = cgrades_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0).to_numpy()
        weights_numeric = cweights_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0).to_numpy()

        # Calculate the product rounded as specified
        total_grades = np.round((grades_numeric * weights_numeric / 100).sum(axis=1))

        # Insert course names back
        result_df = pd.DataFrame({
            "course_number": np.arange(1, len(total_grades) + 1),
            "course_name": cgrades_df["course"].values,
            "grade": total_grades
        })
        filtered_grades = result_df[result_df["grade"] > 59]

        filtered_grades.to_csv(current_results_file, index=False)

        average_filtered_grade = filtered_grades["grade"].mean()
        if debug:
            print("Optimized Average is: {:.2f}".format(average_filtered_grade))
            print(filtered_grades)
        return filtered_grades, average_filtered_grade
    else:
        raise ValueError("The columns in the grades and weights files do not match.")


def get_improvements_options(grades_df: pd.DataFrame, weights_df: pd.DataFrame, current_avg: float, result_count: int = 3) -> pd.DataFrame:
    grades_df_usage = grades_df.copy()
    weights_df_usage = weights_df.copy()
    grade_improvement_options = []

    # print(current_df_usage)
    for index, row in grades_df_usage.iterrows():
        course_name = row['course']
        for increase in [10.0, 15.0, 20.0, 25.0]:
            # Check only the 'exam' column
            if pd.notna(row['exam']) and row['exam'].isdigit():
                if float(increase) + float(row['exam']) < 101.0:
                    # backup current and see possible adjust
                    backup_grades = grades_df_usage.loc[index, :].copy()
                    adjusted_grades = grades_df_usage.loc[index, :]
                    adjusted_grades['exam'] = float(row['exam']) + increase
                    _, new_average = get_current_average(grades_df_usage, weights_df_usage)

                    # Capture only improvements
                    if new_average > current_avg:
                        grade_improvement_options.append({
                            'course': course_name,
                            'new_grade_needed': float(row['exam']),
                            'new_average': new_average,
                            'increase': increase
                        })
                    grades_df_usage.loc[index, :] = backup_grades

    # Convert to DataFrame and find the top 3 options
    improvement_df = pd.DataFrame(grade_improvement_options)
    improvement_df = improvement_df.sort_values(by='new_average', ascending=False)
    improvement_df.to_csv(improved_results_file)
    top_3_improvements = improvement_df.head(result_count)
    return top_3_improvements


if __name__ == '__main__':
    current_result_df, result_avg = get_current_average(basic_grades_df, basic_weights_df, True)
    improvement = get_improvements_options(basic_grades_df, basic_weights_df, result_avg, 5)
    for improvement_index, improvement_row in improvement.iterrows():
        print(f"If you score {improvement_row['new_grade_needed']} ({improvement_row['increase']} more)"
              f"\n in {improvement_row['course']}"
              f"\n The Average will increase by: {improvement_row['new_average'] - result_avg}\n")
