import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

import streamlit as st
import pandas as pd

# --- GLOBAL PAGE STYLE ---
st.markdown("""
    <style>
    /* Page background */
    .stApp {
        background-color: #0b1e39; /* dark blue */
    }

    /* KPI CARD */
    .kpi-card {
        background: #ffffff10;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ffffff20;
        backdrop-filter: blur(10px);
        color: white;
    }

    .kpi-value {
        font-size: 32px;
        font-weight: 700;
        margin-top: -10px;
    }

    .kpi-label {
        font-size: 15px;
        opacity: 0.8;
    }
    </style>
""", unsafe_allow_html=True)


st.title("📈 Business Overview")


total_orders=len(orders['order_id'])
total_revenue=round(orders['price_usd'].sum()/1000000,2)
total_profit=round((orders['price_usd'].sum()-orders['cogs_usd'].sum())/1000000,2)
AOV=orders['price_usd'].sum()/total_orders
refund_rate=len(refunds['order_item_refund_id'])*100/total_orders
cvr=total_orders*100/len(sessions['website_session_id'])
total_customers=orders['user_id'].nunique()
repeat_customers = (orders['user_id'].value_counts() > 1).sum()
items_per_order=len(items['order_item_id'])/total_orders
total_margin=(orders['price_usd'].sum()-orders['cogs_usd'].sum())/(orders['price_usd'].sum())

#-kpis--------------
col1,col2,col3,col4,col5,col6=st.columns(6)
#col1.metric('Total Orders',round(total_orders/1000,2),"k")
#col2.metric('Total Revenue',total_revenue,"M")
#col3.metric('Total Profit',total_profit,"M")
#col4.metric('Avg Order Value',round(AOV,2),"$")
#col5.metric('Refund Rate',round(refund_rate,2),"%")
#col6.metric('Coversion Rate',round(cvr,2),"%")

#col1.metric('Total Customers',round(total_customers/1000,2),"k")
#col2.metric('Repeat Customers',repeat_customers)
#col3.metric('Items per Order',round(items_per_order,2),"units")
#col4.metric('Total Margin',round(total_margin*100,2),"%")

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Orders</div>
            <div class="kpi-value">{total_orders:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Revenue</div>
            <div class="kpi-value">{total_revenue:,.2f}M</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Profit</div>
            <div class="kpi-value">{total_profit:,.2f}M</div>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Order Value</div>
            <div class="kpi-value">{AOV:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Refund Rate</div>
            <div class="kpi-value">{refund_rate:,.2f}%</div>
        </div>
    """, unsafe_allow_html=True)
with col6:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Conversion Rate</div>
            <div class="kpi-value">{cvr:,.2f}%</div>
        </div>
    """, unsafe_allow_html=True)




