import streamlit as st
import pandas as pd

st.set_page_config(page_title="Digital Analytics Dashboard", layout="wide")

# ------------------------------
# LOAD DATA FROM GOOGLE DRIVE
# ------------------------------
@st.cache_data
def load_data():

    url_sessions = "https://drive.google.com/uc?export=download&id=1ajuAwYDnG78lu5pk0Y3_gc6r-m9kbEkz"
    url_pageviews = "https://drive.google.com/uc?export=download&id=1NFDWdWzxY2GxtFXdcGXnksWrCblNKa6T"
    url_products = "https://drive.google.com/uc?export=download&id=1mxpg1D7Q8aYX85yO_-WyjY14JTRkDZnH"
    url_orders = "https://drive.google.com/uc?export=download&id=19_UTwIKYRYyxTN5nTHtN5zIZthMdbaTr"
    url_items = "https://drive.google.com/uc?export=download&id=1UQlE-HZHeOD9AZwGVWY5UdQaSKKZwV77"
    url_refunds = "https://drive.google.com/uc?export=download&id=1au0qZVSF7Z3Gb4riDuCjkJ1D61--M9Kn"

    df_sessions = pd.read_csv(url_sessions)
    df_pageviews = pd.read_csv(url_pageviews)
    df_products = pd.read_csv(url_products)
    df_orders = pd.read_csv(url_orders)
    df_items = pd.read_csv(url_items)
    df_refunds = pd.read_csv(url_refunds)

    return df_sessions, df_pageviews, df_products, df_orders, df_items, df_refunds


df_sessions, df_pageviews, df_products, df_orders, df_items, df_refunds = load_data()


# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Go to page:",
    ["Welcome", "Business Overview", "Product Analysis", "Website Analysis", "Marketing Analysis"]
)


# ------------------------------
# PAGE 1: WELCOME
# ------------------------------
if page == "Welcome":
    st.title("👋 Welcome to Digital Analytics Dashboard")
    st.write(
        """
        This interactive dashboard helps you analyze:

        - 🏢 **Business Overview**
        - 📦 **Product Performance**
        - 🌐 **Website Behaviour**
        - 🎯 **Marketing Channel Performance**

        Use the left navigation panel to explore all sections.
        """
    )

    


# ------------------------------
# PAGE 2: BUSINESS OVERVIEW
# ------------------------------
elif page == "Business Overview":
    st.title("🏢 Business Overview")
    Total_Revenue = df_orders["price_usd"].sum()
    Total_Revenue_M = Total_Revenue / 1_000_000
    st.write("- Total Revenue (in Millions):", round(Total_Revenue_M, 2),"M")
    Total_orders=df_orders["order_id"].nunique()
    st.write("- Total Orders",round((Total_orders/1000),2),"K")
    Aov=df_orders["price_usd"].sum()/Total_orders
    st.write("- Average Order Value (AOV)",round(Aov,2),"$")
    refund_rate=df_refunds["order_item_refund_id"].nunique()*100/ Total_orders
    st.write("- Refund Rate",round(refund_rate,2),"%")
    cvr=Total_orders*100/df_sessions["website_session_id"].nunique()
    st.write("- Conversion Rate",round(cvr,2),"%")

    # Example KPI (you can replace later)
    st.subheader("Sample KPI")
    total_orders = df_orders["order_id"].nunique()
    st.metric("Total Orders", total_orders)



# ------------------------------
# PAGE 3: PRODUCT ANALYSIS
# ------------------------------
elif page == "Product Analysis":
    st.title("📦 Product Analysis")

    st.write("Show charts like:")
    st.write("- Top selling products")
    st.write("- Revenue by category")
    st.write("- Refunds by product")
    st.write("- Product conversion funnel")

    st.dataframe(df_products.head())



# ------------------------------
# PAGE 4: WEBSITE ANALYSIS
# ------------------------------
elif page == "Website Analysis":
    st.title("🌐 Website Behaviour Analysis")

    st.write("You can show:")
    st.write("- Sessions trend")
    st.write("- Pageview trend")
    st.write("- Bounce rate")
    st.write("- Popular landing pages")
    st.write("- Device performance")

    st.dataframe(df_sessions.head())



# ------------------------------
# PAGE 5: MARKETING ANALYSIS
# ------------------------------
elif page == "Marketing Analysis":
    st.title("🎯 Marketing Channel Analysis")

    st.write("Show insights like:")
    st.write("- Traffic by channel")
    st.write("- Conversion by channel")
    st.write("- CPA, CAC metrics")
    st.write("- Channel-wise revenue & ROI")

    st.dataframe(df_pageviews.head())

