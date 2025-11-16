import streamlit as st
import pandas as pd

st.set_page_config(page_title="Digital Analytics", layout="wide")

st.title("Digital Analytics Dashboard")
st.write("Upload a CSV file to begin your analysis!")

uploaded = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("Preview of your data:")
    st.dataframe(df.head())
