import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

st.title("📈 Business Overview")


total_orders=len(orders['order_id'])
total_revenue=round(orders['price_usd'].sum()/1000000,2)
total_profit=round((orders['price_usd'].sum()-orders['cogs_usd'].sum())/1000000,2)
AOV=(orders['price_usd'].sum())*100/total_orders
refund_rate=len(refunds['order_item_refund_id'])*100/total_orders
cvr=total_orders*100/len(sessions['website_session_id'])


#-kpis--------------
col1,col2,col3,col4,col5,col6=st.columns(6)
col1.metric('Total Orders',total_orders)
col2.metric('Total Revenue',total_revenue,"M")
col3.metric('Total Profit',total_profit,"M")
col4.metric('Avg Order Value',round(AOV,2),"M")
col5.metric('Refund Rate',round(refund_rate,2),"%")
col6.metric('Coversion Rate',round(cvr,2),"%")


