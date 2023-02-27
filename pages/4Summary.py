import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np


'''
Summary
---------------------------------
---------------------------------
'''


# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')