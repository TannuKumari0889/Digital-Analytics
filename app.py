import streamlit as st
import pandas as pd
import plotly.express as px
   

st.set_page_config(page_title="Digital Analytics Dashboard", layout="wide")


# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.markdown("<h2 style='text-align:center;'>📊 Dashboard Navigation</h2>", unsafe_allow_html=True)

# Define pages with icons
pages = {
    "🏠 Home": "Home",
    "📌 Business Overview": "Business Overview",
    "🛒 Product Analysis": "Product Analysis",
    "🌐 Website Analysis": "Website Analysis",
    "📊 Marketing Analysis": "Marketing Analysis"
}

# Radio buttons for navigation
page_choice = st.sidebar.radio("Select Page:", list(pages.keys()), index=0)

# Map selection to actual page name
current_page = pages[page_choice]

st.sidebar.markdown("---")  # separator

# Optional info or instructions
st.sidebar.info("Use the sidebar to navigate between pages. Icons make it easier to identify each section.")
czz-gksf-woh


