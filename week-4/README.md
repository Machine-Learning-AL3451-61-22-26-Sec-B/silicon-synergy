# Naive Bayesian Classifier

This repository contains an implementation of a Naive Bayesian classifier. The classifier is trained on a sample dataset stored in a .CSV file and evaluated using several test datasets to compute accuracy.

## Project Overview

The goal of this project is to:
1. Implement a Naive Bayesian classifier.
2. Train the classifier using a sample training dataset stored as a .CSV file.
3. Compute the accuracy of the classifier using a few test datasets.

## Repository Structure

naive-bayes-classifier/
├── data/
│ ├── train.csv
│ └── test1.csv
│ └── test2.csv
│ └── test3.csv
├── naive_bayes.py
├── train.py
├── test.py
├── requirements.txt
└── README.md


- `data/`: Directory containing the training and test datasets.
- `naive_bayes.py`: Implementation of the Naive Bayesian classifier.
- `train.py`: Script to train the classifier.
- `test.py`: Script to test the classifier and compute accuracy.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: Project documentation.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- NumPy
- Pandas
- Scikit-learn

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/naive-bayes-classifier.git
    ```
2. Navigate to the project directory:
    ```sh
    cd naive-bayes-classifier
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

#### Training the Classifier

To train the Naive Bayesian classifier, run:
```sh
python train.py


Testing the Classifier
To test the trained classifier and compute accuracy, run:

sh
Copy code
python test.py



Implementation Details
The Naive Bayesian classifier is implemented using the Gaussian Naive Bayes algorithm. The classifier is trained using the provided training dataset, and its performance is evaluated on several test datasets.


Medium Link: https://medium.com/@sreeleka647/naive-bayesian-classifier-89d55baf0182

