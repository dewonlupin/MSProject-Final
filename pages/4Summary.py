import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objs as go
from plotly_calplot import calplot
import random
import pandas as pd
import numpy as np

from Utilities.SummaryHelper import CalProc

import datetime
np.random.seed(1)


'''
Summary
---------------------------------
---------------------------------
'''


# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')

# creating five column
col_a, *_, col_b= st.columns(5)

# Define 4 values
values = [1, 0, -1, -2]

year = col_b.selectbox("Pick a date", ["2021", "2022", "2023"])

# Create date range
start_date = year+"-01-01"
end_date = year+"-12-31"

days = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days + 1


# condition = [((i*0)-10) for i in range(0, days)]
condition = [10 if i %9 == 0 else None for i in range(0, days)]

# ---------------------- Import dataframe generated from QLA -----------------
path = "Utilities/user_data.csv"
user_data = pd.read_csv(path)


# --------------------- Create a single valued for the list ------------------
cal = []

init = CalProc()
data_init = init.data_reset(cal, days)

# -------------- Copy data from dataframe to list with given index -----------
cond = init.assign_data(user_data, data_init)

# ------------------- Import list into the main dataframe --------------------
dummy_df = pd.DataFrame(
    {
        "ds": pd.date_range(start_date, end_date),
        "value": cond
    }
)


# -------------------------- Create a calendar plot --------------------------
fig = calplot(
    dummy_df,
    x="ds",
    y="value",
    colorscale=["green","yellow", "orange", "red","black"],     #   blackbody inferno
    gap=.3,
    month_lines_width=2,
    month_lines_color="#fff",
    name="Condition"

)
fig.update_layout(
    autosize=False,
    width=800,
    height=300,
    margin=dict(
        l=0,
        r=5,
        b=120,
        t=0,
        pad=0
    ),
    )

fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor= 'rgba(0,0,0,0)')
col_a.write("Overall Condition")

if year in user_data["Date"][0] and year in user_data["Date"][len(user_data)-1]:
    st.plotly_chart(fig)
else:
    st.write("No preview available")