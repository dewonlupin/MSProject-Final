import altair as alt
from vega_datasets import data
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go


# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')


st.title("Nutritients Intake")

with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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


sodium = np.random.randint(low = 200,high=650,size=31)
kcal = np.random.randint(low = 350,high=700,size=31)
water = np.random.randint(low = 300,high=650,size=31)
fat = np.random.randint(low = 20,high=70,size=31)
protein = np.random.randint(low = 20,high=65,size=31)
fiber = np.random.randint(low = 10,high=25,size=31)
carbs = np.random.randint(low = 100,high=200,size=31)

chart_data2 = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)':water, 'Calories(Kcal)': kcal, 'Calories(Kcal)': kcal, 'fat':fat, "Protein":protein, "fiber":fiber, "Carbohydrates":carbs})



st.write("---")
st.header("Monthly overall nutritional data")
st.bar_chart(chart_data2)

#just a space
st.write("---")
col_a, col_b = st.columns(2, gap="medium")


#random data for Nutrition pie chart
sodium = np.random.randint(low = 200,high=650,size=31)
kcal = np.random.randint(low = 350,high=700,size=31)
water = np.random.randint(low = 300,high=650,size=31)

chart_data = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)':water, "kcal": kcal})

scol1, scol2, scol3= st.sidebar.columns(3, gap="small")



st.write("---")
if scol2.button("Monthly"):
    # Code to display the heart rate chart
    chart_data = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)': water, "kcal": kcal})

if scol3.button("Protein"):
    # Code to display the medication schedule
    chart_data = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)': water, "kcal": kcal})

if scol1.button("Calories"):
    # Code to display the nutrition information
    chart_data = pd.DataFrame({'Sodium(cg)': sodium, 'Water(ml)': water, "kcal": kcal})


with col_a:
    st.header("WCS intake")
    st.line_chart(chart_data)


with col_b:
    #lower second level column Pie chart
    labels = ['Fat', 'Carbohydrate', 'Protien', 'Fiber']
    values = [15, 30, 45, 10]

    # The plot
    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hoverinfo="label+percent",
            textinfo="value"
        ))
    #fig.update_layout(legend=dict(y=0.5))

    st.header("Macro chart")
    st.plotly_chart(fig)
