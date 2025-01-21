import sys
import pandas as pd
import matplotlib.pyplot as plt

# Get filenames from command line arguments
filename1 = sys.argv[1]
filename2 = sys.argv[2]

# Load data from the provided files
data1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1,
                    names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1,
                    names=['lang', 'page', 'views', 'bytes'])

# Plot 1: Pareto distribution of views
sorted_views = data1['views'].sort_values(ascending=False)

plt.figure(figsize=(10, 5))  # Set up figure size

# First subplot: Pareto distribution
plt.subplot(1, 2, 1)
plt.plot(sorted_views.values)  # Use the sorted view counts
plt.title("Popularity Distribution")
plt.xlabel("Rank")
plt.ylabel("Views")

# Plot 2: Log-scale scatterplot of hourly views
merged_data = pd.DataFrame({
    'views1': data1['views'],
    'views2': data2['views']
}).dropna()  # Combine data from both files and remove NaN entries

# Second subplot: Log-scale scatterplot
plt.subplot(1, 2, 2)
plt.scatter(merged_data['views1'], merged_data['views2'])
plt.xscale('log')  # Apply log scale to x-axis
plt.yscale('log')  # Apply log scale to y-axis
plt.title("Hourly Correlation")
plt.xlabel("Views (Hour 1)")
plt.ylabel("Views (Hour 2)")

# Save the output as wikipedia.png
plt.tight_layout()
plt.savefig('wikipedia.png')
