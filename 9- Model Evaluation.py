# Check for linearity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.title('Actual vs Predicted Claim Status')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

# Plot residuals
residuals = y_test - y_pred
sns.histplot(residuals, kde=True)
plt.title('Residuals Distribution')
plt.show()

# Q-Q plot for normality check
import scipy.stats as stats
stats.probplot(residuals, dist="norm", plot=plt)
plt.show()

# Check for homoscedasticity
sns.scatterplot(x=y_pred, y=residuals)
plt.title('Predicted vs Residuals')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.show()
