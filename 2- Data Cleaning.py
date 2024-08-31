# Import necessary libraries
import pandas as pd
import numpy as np

# Read the data from the CSV file
data = pd.read_csv('tiktok_dataset.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Drop rows with missing values
data_cleaned = data.dropna()

# Verify the data after cleaning
print("\nDataset Information after cleaning:")
print(data_cleaned.info())
