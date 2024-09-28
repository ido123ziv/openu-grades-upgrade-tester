import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file and select the top 10 rows
results_file = "outputs/improved_result.csv"
result_df = pd.read_csv(results_file).head(10)  # Modify the number of rows as needed

# Create a bar chart showing the frequency of the top grades
plt.figure(figsize=(10, 6))
plt.bar(result_df['course'], result_df['new_grade_needed'], color='skyblue')
plt.title("Top 10 Courses - Grade Frequency")
plt.xlabel("Course Name")
plt.ylabel("Grades")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image
plt.savefig("visualizations/top_10_grades.png")

# Show the plot
plt.show()
