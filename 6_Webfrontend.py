#Task 5: 6) Implementation of simple Webfrontend

import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="PageRank: Disease Pathways in the Human Interactome", layout="wide")

#HEADER SECTION

st.title("Visualizing Dataset")
st.header("Subset Dataset: Human protein-protein interaction network ")
st.subheader('Subset of Dataset')
og_data = Image.open('og_data.png')
st.image(og_data)
st.write('Due to computational resources I have depicted here only 500 of the 342,353 edges. '
         'But we can already see that it is a well connected graph')
st.subheader('Smaller subset of Dataset')
og_data2 = Image.open('og_data2.png')
st.image(og_data2, caption="This shows the first 50 entries")
st.write('Here we only see the first 10 data entries as a table')
df = pd.read_csv('bio-pathways-network.csv',nrows=10)
st.table(df)

st.title("Evaluation of two PageRanking algorithms: Basic and personalized algorithm")
st.subheader('Basic PageRank vs. personalized PageRank')
st.write('A comparison was done using the Kendall tau metric, with which we get a value, as shown below')
ktau = Image.open('Kendall tau.png')
st.image(ktau, caption="This shows the first 50 entries")

st.write('A comparison was done also using descriptive statistical data')
descript = Image.open('Descriptive Comparison.png')
st.image(descript, caption="This is for all data points")
