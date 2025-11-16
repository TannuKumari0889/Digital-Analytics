import streamlit as st
import pandas as pd

# -------- LOAD YOUR 6 TABLES AUTOMATICALLY ----------
@st.cache_data
def load_data():
    df_refund = pd.read_csv("data/order_item_refunds.csv")  # corrected name
    df_items = pd.read_csv("data/order_items.csv")
    df_orders = pd.read_csv("data/orders.csv")
    df_products = pd.read_csv("data/products.csv")
    df_pageviews = pd.read_csv("data/website_pageviews.csv")
    df_sessions = pd.read_csv("data/website_sessions_cleaned.csv")
    return df_refund, df_items, df_orders, df_products, df_pageviews, df_sessions

df_refund, df_items, df_orders, df_products, df_pageviews, df_sessions = load_data()

# --------- SIDEBAR NAVIGATION -----------
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Welcome Page", "Business Overview", "Product Analysis", "Website Analysis", "Marketing Analysis"]
)

# --------- PAGE 1: WELCOME PAGE -----------
if page == "Welcome Page":
    st.title("👋 Welcome to Digital Analytics App")
    st.write("Use the left sidebar to navigate across dashboards.")
    st.write("This app uses your 6 tables to generate business insights.")

# --------- PAGE 2: BUSINESS OVERVIEW -----------
elif page == "Business Overview":
    st.title("📊 Business Overview")

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", len(df_orders))
    col2.metric("Total Products", len(df_products))
    col3.metric("Total Sessions", len(df_sessions))

    # Revenue Trend
    if "price_usd" in df_orders.columns:
        st.subheader("Revenue Over Time")
        df_orders["created_at"] = pd.to_datetime(df_orders["created_at"])
        revenue = df_orders.groupby(df_orders["created_at"].dt.date)["price_usd"].sum()
        st.line_chart(revenue)

# --------- PAGE 3: PRODUCT ANALYSIS -----------
elif page == "Product Analysis":
    st.title("📦 Product Analysis")

    df_merged = df_items.merge(df_products, on="product_id", how="left")

    st.subheader("Top 10 Products by Revenue")
    top_products = (
        df_merged.groupby("product_name")["price_usd"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_products)

# --------- PAGE 4: WEBSITE ANALYSIS -----------
elif page == "Website Analysis":
    st.title("🌐 Website Analytics")

    df_pageviews["created_at"] = pd.to_datetime(df_pageviews["created_at"])
    views_per_day = df_pageviews.groupby(df_pageviews["created_at"].dt.date)["website_pageview_id"].count()

    st.subheader("Daily Website Pageviews")
    st.line_chart(views_per_day)

# --------- PAGE 5: MARKETING ANALYSIS -----------
elif page == "Marketing Analysis":
    st.title("📣 Marketing Performance")

    st.subheader("Sessions by UTM Source")
    utm = df_sessions.groupby("utm_source")["website_session_id"].count()
    st.bar_chart(utm)
