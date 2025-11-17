import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

st.title('🌐Website Analysis')

## KPI's Calculations--------------------
##-----------------------------------------
total_sessions=len(sessions['website_session_id'])

bounces=(pageviews['website_session_id'].value_counts()==1).sum()
bounce_rate=bounces/total_sessions*100

page=pageviews.sort_values(['website_session_id','created_at'])
entry=page.groupby('website_session_id').first()['pageview_url']
top_entry_page=entry.value_counts().idxmax()

exit = pageviews.groupby('website_session_id').last()['pageview_url']
top_exit_page = exit.value_counts().idxmax()


top_traffic_source=sessions['utm_source'].value_counts().idxmax()


col1,col2,col3=st.columns(3)
col1.metric('Total Sessions',total_sessions)
col2.metric('Bounce Rate',round(bounce_rate,2),"%")
col3.metric('Top Entry Page',top_entry_page)
col4.metric('Top Exit Page',top_exit_page)


col1.metric('Top Traffic Source',top_traffic_source)
col2.metric('Top Exit Page',top_exit_page)
