import streamlit as st
import pandas as pd


df_pairs = pd.read_csv("pairs.csv", sep = ";")
st.write(df_pairs)

exchange = st.sidebar.radio("Select an exchange", df_pairs["exchange"].unique())
base_asset = st.sidebar.radio("Base Asset", ["BTC", "ETH"])
