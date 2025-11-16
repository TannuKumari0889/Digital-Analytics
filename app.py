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

    # ---- Centered Title ----
    st.markdown("<h1 style='text-align: center;'>🏢 Business Overview</h1>", unsafe_allow_html=True)
    st.write("")  # spacing

    # ---- KPI Calculations ----
    Total_Revenue = df_orders["price_usd"].sum()
    Total_Revenue_M = Total_Revenue / 1_000_000

    Total_orders = df_orders["order_id"].nunique()

    AOV = df_orders["price_usd"].sum() / Total_orders

    refund_rate = df_refunds["order_item_refund_id"].nunique() * 100 / Total_orders

    cvr = Total_orders * 100 / df_sessions["website_session_id"].nunique()

   Total_Profit = (df_orders["price_usd"] - df_orders["cogs_usd"]).sum()
    Total_Profit_M = Total_Profit / 1_000_000

    # ---- KPI CARD STYLING ----
    st.markdown("""
        <style>
        .kpi-card {
            padding: 20px;
            border-radius: 12px;
            background-color: #f0f2f6;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            margin: 10px;
        }
        .kpi-title {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .kpi-value {
            font-size: 28px;
            font-weight: bold;
            color: #2e86de;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---- 3 KPI cards in a row ----
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='kpi-card'><div class='kpi-title'>Total Revenue</div>"
            f"<div class='kpi-value'>{round(Total_Revenue_M,2)} M</div></div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='kpi-card'><div class='kpi-title'>Total Orders</div>"
            f"<div class='kpi-value'>{round(Total_orders/1000,2)} K</div></div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='kpi-card'><div class='kpi-title'>Average Order Value</div>"
            f"<div class='kpi-value'>${round(AOV,2)}</div></div>",
            unsafe_allow_html=True
        )

    # ---- second row ----
    col4, col5,col6 = st.columns(3)

    with col4:
        st.markdown(
            f"<div class='kpi-card'><div class='kpi-title'>Refund Rate</div>"
            f"<div class='kpi-value'>{round(refund_rate,2)}%</div></div>",
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"<div class='kpi-card'><div class='kpi-title'>Conversion Rate</div>"
            f"<div class='kpi-value'>{round(cvr,2)}%</div></div>",
            unsafe_allow_html=True
        )
         
    with col6:
        st.markdown(
            f"""
            <div class='card'>
                <h3>Total Profit</h3>
                <p>${round(Total_Profit_M, 2)} M</p>
            </div>
            """,
            unsafe_allow_html=True
        )







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

