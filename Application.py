# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:21:07 2025

@author: hp
"""
pip install openpyxl
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt



data=pd.read_excel("Bitcoin_data.xlsx")

data["Date"]=pd.to_datetime(data["Date"])
data.drop(['Unnamed: 0'], axis=1, inplace=True)

col1, col2, col3,col4, col5,col6 ,col7, col8,col9= st.columns([1, 2, 3,4,5,6,7,8,9])

st.title("Prix de Bitcoin en $")
# Adding elements to the first column

# st.header("This is the header")
with col9:
    st.image("bitcoin.webp",width=80)
# st.subheader("This is the subheader")
# st.caption("This is the caption")

st.markdown("Detail des prix du Bitcoin")
data

st.markdown("Evolution du prix du Bitcoin")

st.line_chart(data, x="Date", y="Close")
#date = st.date_input("Pick a date")
