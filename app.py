import streamlit as st
import pandas as pd
import plotly.express as px
   

st.set_page_config(page_title="Digital Analytics Dashboard", layout="wide")






# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Go to page:",
    ["Home", "Business Overview", "Product Analysis", "Website Analysis", "Marketing Analysis"]
)


