"COVID-19 Bayesian Network Diagnosis with Streamlit"

This project demonstrates a Bayesian Network applied to a simplified COVID-19 dataset. The dataset contains aggregated data for different countries, and the Bayesian Network is used to infer the probability of infection based on the date.

"Features"

Loads and preprocesses the COVID-19 dataset.
Constructs a Bayesian Network to model relationships between features.
Fits the Bayesian Network using the Maximum Likelihood Estimation method.
Performs inference to predict the probability of infection on a given date.
Interactive user interface using Streamlit for visualization and inference.
Requirements

To run this project, you'll need the following libraries installed:
streamlit
pandas
scikit-learn
pgmpy
networkx
pydot

You can install these dependencies using pip:
'pip install streamlit pandas scikit-learn pgmpy networkx pydot'

How to Run
Save the code in a Python file, e.g., covid_bayesian_network.py.
Open a terminal and navigate to the directory containing the file.
Run the Streamlit app using the following command:

'streamlit run covid_bayesian_network.py'
A new tab will open in your default web browser displaying the Streamlit app.

"Dataset"
The dataset used is the COVID-19 dataset from datasets/covid-19 on GitHub. It contains aggregated COVID-19 data for different countries, including confirmed cases, deaths, and recoveries.
