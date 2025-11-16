import streamlit as st
import pandas as pd

st.title("Digital Analytics Dashboard ")

st.write("Upload all six tables below:")

orders = st.file_uploader("Upload orders.csv", type=["csv"])
order_items = st.file_uploader("Upload order_items.csv", type=["csv"])
refunds = st.file_uploader("Upload order_items_refund.csv", type=["csv"])
products = st.file_uploader("Upload products.csv", type=["csv"])
pageviews = st.file_uploader("Upload website_pageviews.csv", type=["csv"])
sessions = st.file_uploader("Upload website_sessions_cleaned.csv", type=["csv"])

if orders and order_items and refunds and products and pageviews and sessions:
    st.success("All files uploaded successfully!")

    df_orders = pd.read_csv(orders)
    df_items = pd.read_csv(order_items)
    df_refunds = pd.read_csv(refunds)
    df_products = pd.read_csv(products)
    df_pageviews = pd.read_csv(pageviews)
    df_sessions = pd.read_csv(sessions)

    st.write("### Preview of Orders")
    st.dataframe(df_orders.head())

    st.write("### Preview of Sessions")
    st.dataframe(df_sessions.head())

    st.write("### Tables loaded successfully. Now you can build charts and KPIs.")
else:
    st.info("Please upload all six tables to continue.")

