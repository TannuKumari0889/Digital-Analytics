import streamlit as st
import pandas as pd
import plotly.express as px
   

st.set_page_config(page_title="Digital Analytics Dashboard", layout="wide")



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
            f"<div class='kpi-card'><div class='kpi-title'>Total Profit</div>"
            f"<div class='kpi-value'>${round(Total_Profit_M, 2)} M</div></div>",
            unsafe_allow_html=True
        )
        
        
            
             
            
            
        

        
         
         
     








# -------------------------------
# PAGE 3: PRODUCT ANALYSIS
# -------------------------------
elif page == "Product Analysis":
    st.markdown("<h1 style='text-align: center;'>📦Product Analysis</h1>", unsafe_allow_html=True)
    st.write("")

    # --- PRODUCT KPIs CALCULATION ---

    # TOTAL PRODUCTS
    Total_Products = df_products["product_id"].nunique()

    # BEST & LEAST PERFORMING PRODUCTS (BY REVENUE)
    product_revenue = (
        df_items
        .groupby("product_id")["price_usd"]
        .sum()
        .reset_index()
        .merge(df_products, on="product_id", how="left")
    )

    best_product_row = product_revenue.loc[product_revenue["price_usd"].idxmax()]
    Best_Product = best_product_row["product_name"]
    Best_Product_Revenue = best_product_row["price_usd"]

    least_product_row = product_revenue.loc[product_revenue["price_usd"].idxmin()]
    Least_Product = least_product_row["product_name"]
    Least_Product_Revenue = least_product_row["price_usd"]

    # MOST REFUNDED PRODUCT
    refunds_with_products = (
        df_refunds
        .merge(df_items[["order_item_id", "product_id"]], on="order_item_id", how="left")
        .merge(df_products, on="product_id", how="left")
    )

    refund_amounts = (
        refunds_with_products
        .groupby("product_id")["refund_amount_usd"]
        .sum()
        .reset_index()
        .merge(df_products, on="product_id", how="left")
    )

    most_refunded_row = refund_amounts.loc[refund_amounts["refund_amount_usd"].idxmax()]
    Most_Refunded_Product = most_refunded_row["product_name"]
    Most_Refunded_Amount = most_refunded_row["refund_amount_usd"]

    # --- KPI CARD CSS ---
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
            font-size: 26px;
            font-weight: bold;
            color: #2e86de;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------
    #         KPI GRID: 2 COLUMNS × 2 ROWS
    # ---------------------------------------

    # ROW 1
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Total Products</div>
                <div class='kpi-value'>{Total_Products}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Best Product</div>
                <div class='kpi-value'>{Best_Product}<br>${round(Best_Product_Revenue,2)}</div>
            </div>
            """, unsafe_allow_html=True
        )

    # ROW 2
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Least Product</div>
                <div class='kpi-value'>{Least_Product}<br>${round(Least_Product_Revenue,2)}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Most Refunded Product</div>
                <div class='kpi-value'>{Most_Refunded_Product}<br>${round(Most_Refunded_Amount,2)}</div>
            </div>
            """, unsafe_allow_html=True
        )

    













# -------------------------------
# PAGE: WEBSITE ANALYSIS
# -------------------------------
elif page == "Website Analysis":
    st.markdown("<h1 style='text-align: center;'>🌐 Website Analysis</h1>", unsafe_allow_html=True)
    st.write("")

    # --- KPI CALCULATIONS ---

    # Total Sessions
    Total_Sessions = df_sessions["website_session_id"].nunique()

    # First pageview of each session → Top Entry Page
    first_pageviews = (
        df_pageviews.sort_values(["website_session_id", "created_at"])
        .groupby("website_session_id")
        .first()
        .reset_index()
    )
    top_entry_counts = first_pageviews["pageview_url"].value_counts().reset_index()
    top_entry_counts.columns = ["page", "count"]
    Top_Entry_Page = top_entry_counts.loc[0, "page"]
    Top_Entry_Page_Count = top_entry_counts.loc[0, "count"]

    # Last pageview of each session → Top Exit Page
    last_pageviews = (
        df_pageviews.sort_values(["website_session_id", "created_at"])
        .groupby("website_session_id")
        .last()
        .reset_index()
    )
    top_exit_counts = last_pageviews["pageview_url"].value_counts().reset_index()
    top_exit_counts.columns = ["page", "count"]
    Top_Exit_Page = top_exit_counts.loc[0, "page"]
    Top_Exit_Page_Count = top_exit_counts.loc[0, "count"]

    # Bounce Rate
    pageviews_per_session = df_pageviews.groupby("website_session_id")["website_pageview_id"].count()
    Bounce_Rate = (pageviews_per_session[pageviews_per_session==1].count() / Total_Sessions) * 100

    # Average Pages per Session
    Avg_Pages_Per_Session = df_pageviews.shape[0] / Total_Sessions

    # Top Device Type
    top_device_counts = df_sessions["device_type"].value_counts().reset_index()
    top_device_counts.columns = ["device", "count"]
    Top_Device_Type = top_device_counts.loc[0, "device"]
    Top_Device_Count = top_device_counts.loc[0, "count"]

    # Top UTM Source
    top_utm_source_counts = df_sessions["utm_source"].value_counts().reset_index()
    top_utm_source_counts.columns = ["utm_source", "count"]
    Top_UTM_Source = top_utm_source_counts.loc[0, "utm_source"]
    Top_UTM_Source_Count = top_utm_source_counts.loc[0, "count"]

    # Top UTM Campaign
    top_utm_campaign_counts = df_sessions["utm_campaign"].value_counts().reset_index()
    top_utm_campaign_counts.columns = ["utm_campaign", "count"]
    Top_UTM_Campaign = top_utm_campaign_counts.loc[0, "utm_campaign"]
    Top_UTM_Campaign_Count = top_utm_campaign_counts.loc[0, "count"]

    # --- KPI CARD CSS ---
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
            font-size: 26px;
            font-weight: bold;
            color: #2e86de;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- KPI GRID: 2 ROWS × 4 COLUMNS ---
    cols = st.columns(4)
    kpi_values = [
        ("Total Sessions", Total_Sessions),
        ("Bounce Rate", f"{round(Bounce_Rate,2)}%"),
        ("Top Entry Page", f"{Top_Entry_Page} ({Top_Entry_Page_Count})"),
        ("Top Exit Page", f"{Top_Exit_Page} ({Top_Exit_Page_Count})"),
        ("Avg Pages/Session", round(Avg_Pages_Per_Session,2)),
        ("Top Device Type", f"{Top_Device_Type} ({Top_Device_Count})"),
        ("Top UTM Source", f"{Top_UTM_Source} ({Top_UTM_Source_Count})"),
        ("Top UTM Campaign", f"{Top_UTM_Campaign} ({Top_UTM_Campaign_Count})"),
    ]

    # Display cards in rows
    for i, (title, value) in enumerate(kpi_values):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class='kpi-card'>
                    <div class='kpi-title'>{title}</div>
                    <div class='kpi-value'>{value}</div>
                </div>
                """, unsafe_allow_html=True
            )
        # After 4 columns, reset for next row
        if i % 4 == 3:
            cols = st.columns(4)






# -------------------------------
# PAGE: MARKETING ANALYSIS
# -------------------------------
elif page == "Marketing Analysis":
    st.markdown("<h1 style='text-align: center;'>📈 Marketing Analysis</h1>", unsafe_allow_html=True)
    st.write("")

    # --- KPI CALCULATIONS ---

    # 1️⃣ Total Users Acquired
    Total_Users = df_sessions["user_id"].nunique()

    # 2️⃣ Top UTM Source
    top_source_counts = df_sessions["utm_source"].value_counts().reset_index()
    top_source_counts.columns = ["utm_source", "count"]
    Top_UTM_Source = top_source_counts.loc[0, "utm_source"]
    Top_UTM_Source_Count = top_source_counts.loc[0, "count"]

    # 3️⃣ Top Performing Campaign
    top_campaign_counts = df_sessions["utm_campaign"].value_counts().reset_index()
    top_campaign_counts.columns = ["utm_campaign", "count"]
    Top_UTM_Campaign = top_campaign_counts.loc[0, "utm_campaign"]
    Top_UTM_Campaign_Count = top_campaign_counts.loc[0, "count"]

    # 4️⃣ Conversion Rate by Campaign
    orders_with_campaign = df_orders.merge(df_sessions[["website_session_id", "utm_campaign"]],
                                           on="website_session_id", how="left")
    conv_rate_campaign = (orders_with_campaign.groupby("utm_campaign")["order_id"].nunique() /
                          df_sessions.groupby("utm_campaign")["website_session_id"].nunique() * 100)
    Top_Conv_Campaign = conv_rate_campaign.idxmax()
    Top_Conv_Campaign_Rate = round(conv_rate_campaign.max(), 2)

    # 5️⃣ Average Revenue per Campaign
    revenue_campaign = orders_with_campaign.groupby("utm_campaign")["price_usd"].sum()
    Top_Revenue_Campaign = revenue_campaign.idxmax()
    Top_Revenue_Campaign_Value = round(revenue_campaign.max(), 2)

    # 6️⃣ Bounce Rate by Campaign
    first_pageviews = (
        df_pageviews.sort_values(["website_session_id", "created_at"])
        .groupby("website_session_id")
        .first()
        .reset_index()
    )
    pageviews_per_session = df_pageviews.groupby("website_session_id")["website_pageview_id"].count()
    Bounce_Rate = (pageviews_per_session[pageviews_per_session==1].count() / df_sessions.shape[0]) * 100

    # --- KPI CARD CSS ---
    st.markdown("""
        <style>
        .kpi-card {
            padding: 15px;
            border-radius: 12px;
            background-color: #f0f2f6;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            margin: 10px;
        }
        .kpi-title {
            font-size: 15px;
            font-weight: bold;
            color: #333;
        }
        .kpi-value {
            font-size: 15px;
            font-weight: bold;
            color: #2e86de;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- KPI GRID: 2 ROWS × 3 COLUMNS ---
    cols = st.columns(3)
    kpi_values = [
        ("Total Users Acquired", Total_Users),
        ("Top UTM Source", f"{Top_UTM_Source} ({Top_UTM_Source_Count})"),
        ("Top Campaign (Sessions)", f"{Top_UTM_Campaign} ({Top_UTM_Campaign_Count})"),
        ("Top Campaign (Conversion Rate)", f"{Top_Conv_Campaign} ({Top_Conv_Campaign_Rate}%)"),
        ("Top Campaign (Revenue)", f"{Top_Revenue_Campaign} (${Top_Revenue_Campaign_Value})"),
        ("Overall Bounce Rate", f"{round(Bounce_Rate,2)}%"),
    ]

    # Display cards in rows
    for i, (title, value) in enumerate(kpi_values):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class='kpi-card'>
                    <div class='kpi-title'>{title}</div>
                    <div class='kpi-value'>{value}</div>
                </div>
                """, unsafe_allow_html=True
            )
        # After 3 columns, reset for next row
        if i % 3 == 2:
            cols = st.columns(3)


    # ----------------------
    # 1️⃣ Sessions by UTM Source
    # ----------------------
    
# Example data
source_counts = df_sessions['utm_source'].value_counts().reset_index()
source_counts.columns = ['UTM Source', 'Sessions']
source_counts['Percentage'] = (source_counts['Sessions'] / source_counts['Sessions'].sum() * 100).round(2)

# Create Plotly chart
fig = px.bar(
    source_counts,
    x='UTM Source',
    y='Percentage',
    text='Percentage',
    labels={'UTM Source':'UTM Source', 'Percentage':'% of Total Sessions'},
    color='Percentage'
)
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(yaxis=dict(title='% of Total Sessions'), xaxis=dict(title='UTM Source'))

# ---- Card container ----
st.markdown("""
    <style>
    .chart-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin: 10px 0px;
    }
    .chart-title {
        font-size: 20px;
        font-weight: bold;
        color: #2e86de;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Display chart inside card
st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Percentage of Sessions by UTM Source</div>", unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


 # Chart 2: % Sessions by Campaign
utm_campaign_counts = df_sessions['utm_campaign'].value_counts().reset_index()
utm_campaign_counts.columns = ['Campaign','Sessions']
utm_campaign_counts['Percentage'] = (utm_campaign_counts['Sessions'] / Total_Sessions * 100).round(2)

fig2 = px.bar(
    utm_campaign_counts,
    x='Campaign',
    y='Percentage',
    text='Percentage',
    labels={'Campaign':'Campaign','Percentage':'% of Sessions'},
    color='Percentage',
    color_continuous_scale='Greens'
)
fig2.update_traces(texttemplate='%{text}%', textposition='inside')
fig2.update_layout(title='Percentage of Sessions by Campaign', yaxis_title='% of Sessions', xaxis_title='Campaign')






 


