import pandas as pd

# File paths
grades_file = "grades.csv"
weights_file = "weights.csv"
results_file = 'result.csv'

# Load both files into DataFrames
basic_grades_df = pd.read_csv(grades_file, dtype=str).fillna('')
basic_weights_df = pd.read_csv(weights_file, dtype=str).fillna('')


def get_current_average(grades_df: pd.DataFrame, weights_df: pd.DataFrame, debug=False):
    cgrades_df = grades_df.copy()
    cweights_df = weights_df.copy()
    # Ensure both dataframes have consistent column order
    if set(cgrades_df.columns) == set(cweights_df.columns):
        # Convert to numerical values for calculation, replacing empty strings with zero
        grades_numeric = cgrades_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)
        weights_numeric = cweights_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)

        # Calculate the product rounded as specified
        total_grades = ((grades_numeric * weights_numeric) / 100).sum(axis=1).round()

        # Insert course names back
        result_df = pd.DataFrame({
            "course_number": range(1, len(total_grades) + 1),
            "course_name": cgrades_df["course"],
            "grade": total_grades
        })
        filtered_grades = result_df[result_df["grade"] > 59]

        filtered_grades.to_csv(results_file, index=False)

        average_filtered_grade = filtered_grades["grade"].mean()
        print("Your Average is: {}".format(average_filtered_grade))
        if debug:
            print(filtered_grades)
        return filtered_grades, average_filtered_grade
    else:
        raise ValueError("The columns in the grades and weights files do not match.")


def get_improvements_options(grades_df: pd.DataFrame, weights_df: pd.DataFrame, current_avg: float) -> pd.DataFrame:
    grades_df_usage = grades_df.copy()
    weights_df_usage = weights_df.copy()
    grade_improvement_options = []

    # print(current_df_usage)
    for index, row in grades_df_usage.iterrows():
        course_name = row['course']

        # Check only the 'exam' column
        if pd.notna(row['exam']) and row['exam'].isdigit():
            # backup current and see possible adjust
            backup_grades = grades_df_usage.loc[index, :].copy()
            adjusted_grades = grades_df_usage.loc[index, :]
            adjusted_grades['exam'] = float(row['exam']) + 10
            _, new_average = get_current_average(grades_df_usage, weights_df_usage)

            # Capture only improvements
            if new_average > current_avg:
                grade_improvement_options.append({
                    'course': course_name,
                    'new_grade_needed': float(row['exam']) + 10,
                    'new_average': new_average
                })
            grades_df_usage.loc[index, :] = backup_grades

    # Convert to DataFrame and find the top 3 options
    improvement_df = pd.DataFrame(grade_improvement_options)
    top_3_improvements = improvement_df.sort_values(by='new_average', ascending=False).head(3)
    return top_3_improvements


if __name__ == '__main__':
    current_result_df, result_avg = get_current_average(basic_grades_df, basic_weights_df, True)
    print(get_improvements_options(basic_grades_df, basic_weights_df, result_avg))

