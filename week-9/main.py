import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Locally Weighted Regression function
def locally_weighted_regression(test_point, X_train, y_train, tau):
    m = X_train.shape[0]
    weights = np.exp(-np.sum((X_train - test_point)**2, axis=1) / (2 * tau**2))
    W = np.diag(weights)
    theta = np.linalg.inv(X_train.T @ W @ X_train) @ X_train.T @ W @ y_train
    prediction = test_point @ theta
    return prediction

# Load the Boston Housing dataset from the original source
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Split the data into features (X) and target (y) variables
X = data
y = target

# Add a column of ones to X for the bias term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Dummy train-test split (for demonstration purposes)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Streamlit app
st.title('Locally Weighted Regression')

# Sidebar inputs
tau = st.sidebar.slider('Tau (Bandwidth)', min_value=0.1, max_value=10.0, value=1.0)

# Plot the original data
fig, ax = plt.subplots()
ax.scatter(X_train[:, 12], y_train, color='blue', label='Training Data')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Original Data')
st.pyplot(fig)

# Perform LWR on the test points
predictions = []
for i in range(X_test.shape[0]):
    test_point = X_test[i]
    prediction = locally_weighted_regression(test_point, X_train, y_train, tau)
    predictions.append(prediction)

# Plot the results
fig, ax = plt.subplots()
ax.scatter(X_test[:, 12], y_test, color='red', label='True Values')
ax.scatter(X_test[:, 12], predictions, color='green', label='Predictions')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Locally Weighted Regression Results')
ax.legend()
st.pyplot(fig)
