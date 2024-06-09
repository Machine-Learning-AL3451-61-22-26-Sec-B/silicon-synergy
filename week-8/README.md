# k-Nearest Neighbour (k-NN) Classification of the Iris Dataset

This repository contains a program to implement the k-Nearest Neighbour (k-NN) algorithm to classify the Iris dataset. The program also prints both correct and wrong predictions.

## Prerequisites

- Python 3.x
- Required Python packages:
  - pandas
  - numpy
  - scikit-learn

You can install the necessary packages using:
```sh
pip install pandas numpy scikit-learn

Project Structure
data/: Directory containing the Iris dataset (if not using sklearn's built-in dataset).
scripts/: Directory containing the Python script for classification.
README.md: This file.
Instructions
1. Prepare the Data
If you are using a custom Iris dataset, place the CSV file in the data/ directory. Alternatively, the script can use the built-in Iris dataset from scikit-learn.

2. Run the k-NN Classification Script
To classify the Iris dataset using the k-NN algorithm, run the script knn_classification.py:

python scripts/knn_classification.py
This script will:

Load the Iris dataset.
Split the dataset into training and testing sets.
Apply the k-NN algorithm to classify the test data.
Print both correct and wrong predictions.
Script Overview
scripts/knn_classification.py
This script performs the following steps:

Load Dataset: Loads the Iris dataset from scikit-learn or a CSV file.
Data Preprocessing: Splits the dataset into training and testing sets.
k-NN Classification: Applies the k-NN algorithm to classify the test data.
Evaluation: Prints both correct and wrong predictions, along with their indices

Medium Link: https://medium.com/@roshinimohammed2004/an-investigation-using-the-iris-dataset-to-learn-about-the-k-nearest-neighbors-algorithm-cbd8617bcafb
