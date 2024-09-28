import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file and select the top 10 rows
results_file = "outputs/improved_result.csv"
result_df = pd.read_csv(results_file).head(10)  # Modify the number of rows as needed
result_df = result_df.drop_duplicates(subset='course', keep='first')

# Create a bar chart with `new_grade_needed` values
fig, ax = plt.subplots(figsize=(12, 7))

# Create the base bar for `new_grade_needed`
bars = ax.bar(result_df['course'], result_df['new_grade_needed'], color='skyblue', label='New Grade Needed')

# Overlay another bar with the top segment color for the "increase"
for index, bar in enumerate(bars):
    height = bar.get_height()
    # Add the "increase" value on top of the `new_grade_needed` bar
    ax.bar(
        result_df['course'][index], result_df['increase'][index],
        bottom=height, color='orange', label='Increase' if index == 0 else ""
    )

# Annotate each bar with the "increase" value
for bar, inc in zip(bars, result_df['increase']):
    ax.text(
        bar.get_x() + bar.get_width() / 2, bar.get_height() + inc / 2,
        f'{inc}', ha='center', va='center', fontsize=10, color='black'
    )

# Formatting and labels
plt.title("Top 10 Courses - Grade Frequency with Increase Highlighted")
plt.xlabel("Course Name")
plt.ylabel("Grades")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image
plt.savefig("visualizations/top_10_grades.png")

# Show the plot
plt.show()
