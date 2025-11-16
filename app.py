import streamlit as st
import pandas as pd

st.title("Digital Analytics Dashboard")

st.write("Upload all six tables below in the correct order:")

refunds = st.file_uploader("1. Upload order_items_refund.csv", type=["csv"])
order_items = st.file_uploader("2. Upload order_items.csv", type=["csv"])
orders = st.file_uploader("3. Upload orders.csv", type=["csv"])
products = st.file_uploader("4. Upload products.csv", type=["csv"])
pageviews = st.file_uploader("5. Upload website_pageviews.csv", type=["csv"])
sessions = st.file_uploader("6. Upload website_sessions_cleaned.csv", type=["csv"])

if refunds and order_items and orders and products and pageviews and sessions:
    st.success("All 6 tables uploaded successfully!")

    df_refunds = pd.read_csv(refunds)
    df_items = pd.read_csv(order_items)
    df_orders = pd.read_csv(orders)
    df_products = pd.read_csv(products)
    df_pageviews = pd.read_csv(pageviews)
    df_sessions = pd.read_csv(sessions)

    st.subheader("Preview: orders")
    st.dataframe(df_orders.head())

    st.subheader("Preview: sessions")
    st.dataframe(df_sessions.head())

    st.info("All tables loaded. Tell me when you're ready — I will add KPIs & charts next.")
else:
    st.warning("Please upload all 6 tables to continue.")
