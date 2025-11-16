import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

#total_orders=len(orders['order_id'])
total_revenue=orders['price_usd'].sum()

#-kpis--------------
col1=st.columns(1)
#col1.metirc['Total Orders',total_orders]
col1.metirc['Total Revenue',total_revenue]

