"Naive Bayes Document Classification with Streamlit"

This project demonstrates a simple document classification application using a Naive Bayes classifier to detect spam messages. The dataset used is the SMS Spam Collection from the UCI Machine Learning Repository. The application is built with Streamlit for an interactive user interface.

"Features"

Loads and preprocesses the SMS Spam Collection dataset.
Uses CountVectorizer and TfidfTransformer to convert text data into numerical features.
Trains a Multinomial Naive Bayes classifier on the training data.
Evaluates the model using accuracy, precision, and recall metrics.
Displays sample predictions for user-selected number of messages.

"Requirements"

To run this project, you'll need the following libraries installed:

streamlit
pandas
scikit-learn
requests

You can install these dependencies using pip:
'pip install streamlit pandas scikit-learn requests'

"How to Run"

Save the code in a Python file, e.g., naive_bayes_streamlit.py.
Open a terminal and navigate to the directory containing the file.
Run the Streamlit app using the following command:

'streamlit run naive_bayes_streamlit.py'

A new tab will open in your default web browser displaying the Streamlit app.


Medium Link:https://medium.com/@sivasanjana29/naive-bayesian-classifier-29869defd702
