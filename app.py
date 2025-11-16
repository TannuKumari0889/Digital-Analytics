import streamlit as st
import pandas as pd

# Initialize session state page
if "page" not in st.session_state:
    st.session_state["page"] = "home"

def go_to(page):
    st.session_state["page"] = page
if st.session_state["page"] == "home":
    st.title("Digital Analytics Dashboard")
    st.subheader("Welcome!")

    st.write("Upload all 6 tables to continue:")

    refunds = st.file_uploader("1. order_items_refund.csv", type=["csv"])
    items = st.file_uploader("2. order_items.csv", type=["csv"])
    orders = st.file_uploader("3. orders.csv", type=["csv"])
    products = st.file_uploader("4. products.csv", type=["csv"])
    pageviews = st.file_uploader("5. website_pageviews.csv", type=["csv"])
    sessions = st.file_uploader("6. website_sessions_cleaned.csv", type=["csv"])

    if refunds and items and orders and products and pageviews and sessions:
        st.success("All files uploaded!")

        st.session_state["df_refunds"] = pd.read_csv(refunds)
        st.session_state["df_items"] = pd.read_csv(items)
        st.session_state["df_orders"] = pd.read_csv(orders)
        st.session_state["df_products"] = pd.read_csv(products)
        st.session_state["df_pageviews"] = pd.read_csv(pageviews)
        st.session_state["df_sessions"] = pd.read_csv(sessions)

        st.write("Choose a section to start:")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Business Overview"):
                go_to("overview")
        with col2:
            if st.button("Product Analysis"):
                go_to("product")

        col3, col4 = st.columns(2)
        with col3:
            if st.button("Website Analysis"):
                go_to("website")
        with col4:
            if st.button("Marketing Analysis"):
                go_to("marketing")
    else:
        st.info("Please upload all 6 files.")


if st.session_state["page"] == "overview":
    st.title("Business Overview")

    df_orders = st.session_state["df_orders"]
    df_sessions = st.session_state["df_sessions"]

    st.subheader("Key Metrics")

    total_orders = df_orders["order_id"].nunique()
    total_revenue = df_orders["price_usd"].sum()
    total_users = df_sessions["user_id"].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Orders", total_orders)
    col2.metric("Revenue", round(total_revenue, 2))
    col3.metric("Users", total_users)

    df_orders["date"] = pd.to_datetime(df_orders["created_at"]).dt.date
    trend = df_orders.groupby("date")["order_id"].count()

    st.subheader("Orders Trend")
    st.line_chart(trend)

    if st.button("⬅ Back"):
        go_to("home")


if st.session_state["page"] == "product":
    st.title("Product Analysis")

    df_items = st.session_state["df_items"]
    df_products = st.session_state["df_products"]

    st.subheader("Revenue by Product")

    revenue = df_items.groupby("product_id")["price_usd"].sum()
    st.bar_chart(revenue)

    if st.button("⬅ Back"):
        go_to("home")



if st.session_state["page"] == "website":
    st.title("Website Analysis")

    df_pageviews = st.session_state["df_pageviews"]

    st.subheader("Top Pageviews")
    st.bar_chart(df_pageviews["pageview_url"].value_counts())

    if st.button("⬅ Back"):
        go_to("home")



if st.session_state["page"] == "marketing":
    st.title("Marketing Analysis")

    df_sessions = st.session_state["df_sessions"]

    st.subheader("Traffic by Source")
    st.bar_chart(df_sessions["utm_source"].value_counts())

    if st.button("⬅ Back"):
        go_to("home")
