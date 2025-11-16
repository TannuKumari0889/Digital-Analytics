import streamlit as st 
from data_tables import load_data
sessions, pageviews, products, orders, items, refunds = load_data()
