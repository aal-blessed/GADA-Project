# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read the data from the CSV file
data = pd.read_csv('tiktok_dataset.csv')

# Data cleaning and feature engineering
# For example, converting categorical variables into dummy/indicator variables
data = pd.get_dummies(data, drop_first=True)

# Split the data into features and target variable
X = data.drop('claim_status', axis=1)  # Assuming 'claim_status' is the target variable
y = data['claim_status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (if necessary)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
