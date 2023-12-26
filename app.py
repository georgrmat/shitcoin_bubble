import streamlit as st
import pandas as pd


df_pairs = pd.read_excel("pairs.xlsx")
st.write(df)

exchange = st.sidebar.radio("Select an exchange", df_pairs["exchange"].unique())
base_asset = st.sidebar.radio("Base Asset", ["BTC", "ETH"])