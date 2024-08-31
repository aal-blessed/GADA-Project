from scipy import stats

# Example hypothesis: Do verified users have significantly higher video view counts than non-verified users?

# Separate the data into two groups based on verification status
verified = data[data['verified_status'] == 'verified']['video_view_count']
non_verified = data[data['verified_status'] == 'not verified']['video_view_count']

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(verified, non_verified, nan_policy='omit')

# Display the t-statistic and p-value
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in video view counts between verified and non-verified users.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in video view counts between verified and non-verified users.")
