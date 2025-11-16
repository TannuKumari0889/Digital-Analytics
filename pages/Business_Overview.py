import streamlit as st 
from data_tables.py import load_data
sessions, pageviews, products, orders, items, refunds = load_data()
