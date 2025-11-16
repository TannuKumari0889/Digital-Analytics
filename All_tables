import pandas as pd 
import streamlit as st




# ------------------------------
# LOAD DATA FROM GOOGLE DRIVE
# ------------------------------
@st.cache_data
def load_data():

    url_sessions = "https://drive.google.com/uc?export=download&id=1ajuAwYDnG78lu5pk0Y3_gc6r-m9kbEkz"
    url_pageviews = "https://drive.google.com/uc?export=download&id=1NFDWdWzxY2GxtFXdcGXnksWrCblNKa6T"
    url_products = "https://drive.google.com/uc?export=download&id=1mxpg1D7Q8aYX85yO_-WyjY14JTRkDZnH"
    url_orders = "https://drive.google.com/uc?export=download&id=19_UTwIKYRYyxTN5nTHtN5zIZthMdbaTr"
    url_items = "https://drive.google.com/uc?export=download&id=1UQlE-HZHeOD9AZwGVWY5UdQaSKKZwV77"
    url_refunds = "https://drive.google.com/uc?export=download&id=1au0qZVSF7Z3Gb4riDuCjkJ1D61--M9Kn"

    sessions = pd.read_csv(url_sessions)
    pageviews = pd.read_csv(url_pageviews)
    products = pd.read_csv(url_products)
    orders = pd.read_csv(url_orders)
    items = pd.read_csv(url_items)
    refunds = pd.read_csv(url_refunds)

    return sessions, pageviews, products, orders, items, refunds

