# Import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Display the distribution of numerical variables
data_cleaned.hist(figsize=(10, 8))
plt.show()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data_cleaned.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.show()

# Create a box plot for key variables
plt.figure(figsize=(10, 6))
sns.boxplot(x='verified_status', y='video_view_count', data=data_cleaned)
plt.show()

# Create a scatter plot between two variables
plt.figure(figsize=(10, 6))
sns.scatterplot(x='video_view_count', y='video_like_count', data=data_cleaned)
plt.show()
