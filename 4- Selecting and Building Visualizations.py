# Scatter plot with variable coloring based on author ban status
plt.figure(figsize=(10, 6))
sns.scatterplot(x='video_view_count', y='video_share_count', hue='author_ban_status', data=data_cleaned)
plt.title('Scatter plot of Video View Count vs. Share Count by Author Ban Status')
plt.show()

# Box plot for multiple variables
plt.figure(figsize=(10, 6))
sns.boxplot(x='claim_status', y='video_view_count', data=data_cleaned)
plt.title('Box plot of Video View Count by Claim Status')
plt.show()
