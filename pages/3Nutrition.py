import altair as alt
from vega_datasets import data
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go


# creating title for the Nutrition page
'''
Nutrients Intake
-------------------------
'''


# Create the sidebar
st.sidebar.title("CHF DashBoard")

# Importing Image inside the sidebar
pic = Image.open('Utilities/logo.jpg')

# placing imported image to the sidebar
st.sidebar.image(pic, caption='Luna')


# importing CSS layouts for Nutrition tab
with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write("---")


# Row A
a1, a2, a3 = st.columns(3)
a1.metric("Overall Diet", "Good")
a2.metric("WCS Intake", "Balanced")
a3.metric("Overall Sodium Intake", "Average")


# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Max Calories intake", "800 Kcal")
b2.metric("Max Sodium Intake", "65")
b3.metric("Optimal Macros Ratio", "5:1:2:3")
b4.metric("Max Sodium tolerance", "49 mg")


sodium = np.random.randint(low = 200,high=650,size=31)
kcal = np.random.randint(low = 350,high=700,size=31)
water = np.random.randint(low = 300,high=650,size=31)
fat = np.random.randint(low = 20,high=70,size=31)
protein = np.random.randint(low = 20,high=65,size=31)
fiber = np.random.randint(low = 10,high=25,size=31)
carbs = np.random.randint(low = 100,high=200,size=31)
weight = np.random.randint(low = 30, high = 70, size =31)

# creating a dataframe for the Daily chart
chart_data2 = pd.DataFrame({"Weight": weight,'Sodium(cg)': sodium,
                            'Water(ml)':water, 'Calories(Kcal)': kcal,
                            'Calories(Kcal)': kcal, 'fat':fat,
                            "Protein":protein, "fiber":fiber,
                            "Carbohydrates":carbs})


st.write("---")

# create 2 columns
chart_col, radio_col = st.columns(2, gap= "large")

# one column will have header
chart_col.header("Monthly nutrition")

# other column will have radio button
align_radio = radio_col.radio("",('Daily', 'Weekly', 'Monthly'), horizontal=True)

# if selected Daily radio
if align_radio == 'Daily':
    # size should be 31
    sodium = np.random.randint(low=200, high=650, size=31)
    kcal = np.random.randint(low=350, high=700, size=31)
    water = np.random.randint(low=300, high=650, size=31)
    fat = np.random.randint(low=20, high=70, size=31)
    protein = np.random.randint(low=20, high=65, size=31)
    fiber = np.random.randint(low=10, high=25, size=31)
    carbs = np.random.randint(low=100, high=200, size=31)
    weight = np.random.randint(low=30, high=70, size=31)

    # creating a dataframe for the Daily chart
    Daily_data = pd.DataFrame({"Weight": weight,'Sodium(cg)': sodium,
                               'Water(ml)': water, 'Calories(Kcal)': kcal,
                               'Calories(Kcal)': kcal, 'fat': fat,
                               "Protein": protein, "fiber": fiber,
                               "Carbohydrates": carbs})

    st.bar_chart(Daily_data)

# if selected Weekly radio
if align_radio == 'Weekly':
    # size should be 15
    sodium = np.random.randint(low=200, high=650, size=15)
    kcal = np.random.randint(low=350, high=700, size=15)
    water = np.random.randint(low=300, high=650, size=15)
    fat = np.random.randint(low=20, high=70, size=15)
    protein = np.random.randint(low=20, high=65, size=15)
    fiber = np.random.randint(low=10, high=25, size=15)
    carbs = np.random.randint(low=100, high=200, size=15)
    weight = np.random.randint(low=30, high=70, size=15)

    # creating a dataframe for the Weekly chart
    Weekly_data = pd.DataFrame({"Weight": weight,'Sodium(cg)': sodium,
                                'Water(ml)': water, 'Calories(Kcal)': kcal,
                                'Calories(Kcal)': kcal, 'fat': fat,
                                "Protein": protein, "fiber": fiber,
                                "Carbohydrates": carbs})

    st.bar_chart(Weekly_data)


# if selected Monthly radio
if align_radio == 'Monthly':
    # size should be 12
    sodium = np.random.randint(low=200, high=650, size=12)
    kcal = np.random.randint(low=350, high=700, size=12)
    water = np.random.randint(low=300, high=650, size=12)
    fat = np.random.randint(low=20, high=70, size=12)
    protein = np.random.randint(low=20, high=65, size=12)
    fiber = np.random.randint(low=10, high=25, size=12)
    carbs = np.random.randint(low=100, high=200, size=12)
    weight = np.random.randint(low=30, high=70, size=12)

    # creating a dataframe for the Monthly chart
    Monthly_data = pd.DataFrame({"Weight": weight,'Sodium(cg)': sodium,
                                 'Water(ml)': water, 'Calories(Kcal)': kcal,
                                 'Calories(Kcal)': kcal, 'fat': fat,
                                 "Protein": protein, "fiber": fiber,
                                 "Carbohydrates": carbs})

    # plotting monthly bar chart
    st.bar_chart(Monthly_data)


# just a space
st.write("---")
col_a, col_b = st.columns(2, gap="small")


# number of days
length = 15
# random data for Water, Calories and Sodium (WCS) intake
sodium = np.random.randint(low = 200,high=650,size=length)
kcal = np.random.randint(low = 350,high=700,size=length)
water = np.random.randint(low = 300,high=650,size=length)

# number of days
days = [x for x in range(1,length+1)]

# plotting Water, Calories and Sodium (WCS) intake chart
chart_data = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)':water, "kcal": kcal})


with col_a:
    # lower first level column Pie chart
    st.header("WCS intake")

    # plotting Line chart for WCS    st.line_chart(chart_data)

    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=days, y=water, name='Water',
                  line = dict(color='green', width=2)))
    # adding linechart for Calories
    fig.add_trace(go.Scatter(x=days, y=kcal, name='Calories',
                  line = dict(color='royalblue', width=2)))
    # adding linechart for Sodium
    fig.add_trace(go.Scatter(x=days, y=sodium, name='Sodium(cg)',
                  line = dict(color='firebrick', width=2)))

    # removing x-axis grid lines
    fig.update_xaxes(gridcolor='grey', griddash='dash',
                     minor_griddash="dot", showline=True,
                     mirror=True)

    # removing y-axis grid lines
    fig.update_yaxes(showgrid=False, showline=True)

    # updating the size and alignments of Pie chart
    fig.update_layout(xaxis_title="Days", yaxis_title="Normalize WCS",
                      autosize=False,width=450,height=350,
                      margin=dict(
                          l=1,
                          r=1,
                          b=100,
                          t=1,
                          pad=1
                        ),
                     )

    # plotting the final pie chart
    col_a.plotly_chart(fig)


with col_b:
    # lower second level column Pie chart
    labels = ['Fat', 'Carbohydrate', 'Protein', 'Fiber']
    values = [15, 30, 45, 10]

    # basic initialization of pie chart
    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hoverinfo="label+percent",
            textinfo="percent",
            pull=[0.025, 0.025, 0.025, 0.025]
        ))

    # updating the size and alignments of Pie chart
    fig.update_layout(
        autosize=False,
        width=400,
        height=400,
        margin=dict(
            l=60,
            r=5,
            b=120,
            t=1,
            pad=0
        ),
    )
    fig.update_traces(hole=.4)
    # header of the pie chart
    st.header("Macro chart")

    # plotting the final pie chart
    st.plotly_chart(fig)
