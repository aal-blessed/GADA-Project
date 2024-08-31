# Import necessary libraries for data manipulation and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset into dataframe
# We are reading the TikTok dataset from a CSV file and storing it in a DataFrame.
data = pd.read_csv('tiktok_dataset.csv')

# Display the first few rows of the DataFrame to understand its structure
print("Displaying the first 10 rows of the dataset:")
print(data.head(10))

# Examine data types of each column
# This helps us understand what kind of data we're working with, such as integers, floats, or objects (strings).
print("\nData types of each column:")
print(data.info())

# Gather descriptive statistics to get an overview of the dataset
# This provides summary statistics for numerical columns, such as mean, min, max, and percentiles.
print("\nDescriptive statistics of the dataset:")
print(data.describe())

# Visualize the distribution of numerical variables using histograms
# Histograms help us see the distribution and frequency of data points across different ranges.
data.hist(figsize=(10, 8))
plt.show()

# Visualize the correlation between variables using a heatmap
# A correlation heatmap shows the relationship between variables; closer to 1 or -1 means stronger correlation.
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.show()

# Create a boxplot to explore the relationship between verified status and video view count
# Boxplots are useful for visualizing the spread and outliers in data based on categories.
plt.figure(figsize=(10, 6))
sns.boxplot(x='verified_status', y='video_view_count', data=data)
plt.show()
