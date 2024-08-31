# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('tiktok_dataset.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display the first few rows of the dataset
print("First 10 rows of the dataset:")
print(data.head(10))

# Check for missing values
print("Missing values in each column:")
print(data.isnull().sum())

# Handle missing values if necessary
data_cleaned = data.dropna()
