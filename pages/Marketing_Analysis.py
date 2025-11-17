import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

## KPI's Calculation-----------------------------
-------------------------------------------------
gsearch_sessions=sessions.loc[sessions['utm_source']=='gsearch','website_session_id'].count()
gsearch_cvr = orders['website_session_id'].isin(sessions[sessions['utm_source']=='gsearch']['website_session_id']).sum() / gsearch_sessions*100

repeat_customer=orders['user_id'].value_counts.



col1,col2,col3,col4,col5,col6=st.columns(6)
col1.metric('Gsearch CVR',round(gsearch_cvr,2))
col2.metric()


