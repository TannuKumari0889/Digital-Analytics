import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

st.title("📈 Business Overview")


total_orders=len(orders['order_id'])
total_revenue=round(orders['price_usd'].sum()/1000000,2)


#-kpis--------------
col1,col2=st.columns(2)
col1.metric('Total Orders',total_orders)
col2.metric('Total Revenue',total_revenue,"M")

