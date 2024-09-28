import pandas as pd
import matplotlib.pyplot as plt

# Load the results CSV file
results_file = "result.csv"
result_df = pd.read_csv(results_file)

# Create a histogram for grade frequency
plt.figure(figsize=(10, 6))
plt.hist(result_df['grade'], bins=10, color='skyblue', edgecolor='black')
plt.title("Grade Frequency Distribution")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.grid(axis='y')

# Save the plot as an image
plt.savefig("grade_frequency.png")

# Show the plot
plt.show()
