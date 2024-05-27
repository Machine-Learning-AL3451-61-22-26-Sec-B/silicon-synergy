import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import networkx as nx
from networkx.drawing.nx_pydot import to_pydot

# Load the dataset
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
    data = pd.read_csv(url)
    return data

df = load_data()

# Preprocess the data
# For simplicity, we'll create a subset with relevant features and binary labels
df = df[['Date', 'Country', 'Confirmed', 'Deaths', 'Recovered']]
df = df[df['Country'] == 'US']  # Filter for one country to simplify

# Add a column to represent infection status (1 if Confirmed > 0, else 0)
df['Infected'] = df['Confirmed'].apply(lambda x: 1 if x > 0 else 0)

# Encode categorical data
le = LabelEncoder()
df['Date'] = le.fit_transform(df['Date'])

# Define the Bayesian Network structure
model = BayesianNetwork([
    ('Date', 'Infected'),
    ('Infected', 'Confirmed'),
    ('Confirmed', 'Deaths'),
    ('Confirmed', 'Recovered')
])

# Fit the model to the data
model.fit(df, estimator=MaximumLikelihoodEstimator)

# Perform inference
infer = VariableElimination(model)

# Streamlit app
st.title('COVID-19 Bayesian Network Diagnosis')

st.write('## Dataset')
st.write(df.head())

st.write('## Bayesian Network Structure')

# Manually create a NetworkX graph from the Bayesian Network
nx_graph = nx.DiGraph()
nx_graph.add_edges_from(model.edges())

# Convert NetworkX graph to DOT format for visualization
dot_graph = to_pydot(nx_graph).to_string()
st.graphviz_chart(dot_graph)

st.write('## Inference')
date_input = st.slider('Select Date (encoded)', min_value=int(df['Date'].min()), max_value=int(df['Date'].max()), value=int(df['Date'].min()))

query = infer.map_query(variables=['Infected'], evidence={'Date': date_input})
st.write(f'Probability of Infection on selected date: {query["Infected"]}')

st.write('## Note')
st.write('This is a simplified example. For a real-world application, use more comprehensive and current data, and consider additional relevant features.')
