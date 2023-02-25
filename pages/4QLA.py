
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np


#extracting style sheet
with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')


#title of the page
st.title("Quality of Life assesment")


#assigning columns for metrices
col1, col2, col3 = st.columns(3, gap='medium')

# Row A
a1, a2, a3 = st.columns(3)
a1.metric("Humidity", "1"+"%")
a2.metric("Feels like", "2")
a3.metric("Highest temperature", "4")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Humidity", "1"+"%")
b2.metric("Feels like", "2")
b3.metric("Highest temperature", "4")
b4.metric("Lowest temperature", "5")