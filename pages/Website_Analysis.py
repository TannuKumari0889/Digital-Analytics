import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()

## KPI's Calculations--------------------
-----------------------------------------
total_sessions=len(sessions['website_session_id'])

bounces=(pageviews['website_session_id'].value_counts()==1).sum()
bounce_rate=bounces/total_sessions*100

page=website_pageviews.sort_values(['website_session_id','created_at'])
entry=page.groupby('website_session_id').first()['pageview_url']
top_entry_page=entry.value_counts().idxmax()

page=website_pageviews.sort_values(['website_session_id','created_at'],ascending=False)
exit=page.groupby('website_session_id').first()['pageview_url']
top_exit_page=exit.value_counts().idxmax()

top_traffic_source=website_sessions['utm_source'].value_counts().idxmax()
