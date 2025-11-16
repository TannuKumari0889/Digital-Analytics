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

    # ===== PAGE BACKGROUND COLOR =====
    st.markdown("""
    <style>
    .main {
        background-color: #001f3f !important;  /* Dark Blue */
    }
    </style>
    """, unsafe_allow_html=True)

    # Apply background style
    st.markdown("<style>body {background-color: #001f3f;}</style>", unsafe_allow_html=True)

    # ===== KPI CARD STYLING =====
    st.markdown("""
    <style>
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        text-align: center;
        margin-bottom: 20px;
    }
    .card h3 {
        font-size: 22px;
        margin-bottom: 8px;
        font-weight: 600;
        color: #001f3f;
    }
    .card p {
        font-size: 26px;
        font-weight: bold;
        margin: 0;
        color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

    # ===== PAGE TITLE =====
    st.markdown("<h1 style='text-align: center; font-size: 40px; color: white;'>🏢 Business Overview</h1>", 
                unsafe_allow_html=True)

    # --------------------
    # CALCULATIONS
    # --------------------
    Total_Revenue = df_orders["price_usd"].sum()
    Total_Revenue_M = Total_Revenue / 1_000_000

    Total_orders = df_orders["order_id"].nunique()

    AOV = Total_Revenue / Total_orders

    Total_Profit = (df_orders["price_usd"] - df_orders["cogs_usd"]).sum()
    Total_Profit_M = Total_Profit / 1_000_000

    refund_rate = df_refunds["order_item_refund_id"].nunique() * 100 / Total_orders

    CVR = Total_orders * 100 / df_sessions["website_session_id"].nunique()

    # --------------------
    # KPI CARDS LAYOUT
    # --------------------
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class='card'>
            <h3>Total Revenue</h3>
            <p>${round(Total_Revenue_M, 2)} M</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card'>
            <h3>Total Orders</h3>
            <p>{round(Total_orders/1000, 2)} K</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='card'>
            <h3>Average Order Value</h3>
            <p>${round(AOV, 2)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='card'>
            <h3>Total Profit</h3>
            <p>${round(Total_Profit_M, 2)} M</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class='card'>
            <h3>Refund Rate</h3>
            <p>{round(refund_rate, 2)}%</p>
        </div>
        """, unsafe_allow_html=True)



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

