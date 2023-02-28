import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np


# Page setting
st.set_page_config(
    page_title="CHF: Overview",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Hakuna Matata"
    }
)



# CSS based styling
with open('Utilities/OverviewStyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Create the sidebar
st.sidebar.title("CHF DashBoard")


'''
Overview
-------------------------
'''


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic,width=250, caption='Luna')


#title for the page
st.title("Overview")
st.write("---")



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


#dummy data
df = pd.DataFrame({
    'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'],
    'sodium_intake': [40, 50, 60, 35, 25, 46, 20, 30, 22, 31]
})

# Create the line chart
fig = px.line(df, x='date', y='sodium_intake')

# Add the threshold line
threshold = 45
fig.update_layout(
    shapes=[
        dict(
            type='line',
            x0=df.date.min(),
            x1=df.date.max(),
            y0=threshold,
            y1=threshold,
            yref='y',
            layer='above',
            line=dict(
                color='purple',
                dash='dot'
            )
        )
    ]
)


# Change color of line to red if sodium intake exceeds the threshold
df_over_threshold = df[df.sodium_intake > threshold]
for i, row in df_over_threshold.iterrows():
    fig.add_shape(
        type='line',
        x0=row['date'],
        x1=row['date'],
        y0=0,
        y1=row['sodium_intake'],
        yref='y',
        layer='above',
        line=dict(
            color='red'
        )
    )
# df['threshold'] = df_over_threshold

st.plotly_chart(fig, use_container_width=True)
st.area_chart(df_over_threshold, use_container_width=True)


labels = ['Good', 'Bad', 'Average', 'Critical']
values = [21, 12, 55, 2]


fig4 = px.pie(labels, values = values, hole = 0.4,
              names = labels, color = labels,
              title = 'Overall Health',
              color_discrete_map = {'Good':'green',
                                    'Critical': 'red',
                            'Bad':'purple',
                            'Average':'orange'
             })
fig4.update_traces(
                   title_font = dict(size=25,family='Verdana',
                                     color='darkred'),
                   hoverinfo='label+percent',
                   textinfo='percent', textfont_size=20)

st.plotly_chart(fig4)