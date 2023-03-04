import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Page setting
# st.set_page_config(
#     page_title="CHF: Overview",
#     page_icon=":dog:",
#     layout="wide",
#     initial_sidebar_state="auto",
#     menu_items={
#         'About': "Hakuna Matata"
#     }
# )



# Create the sidebar
st.sidebar.title("CHF DashBoard")

# Importing Image inside the sidebar
pic = Image.open('Utilities/logo.jpg')

# placing imported image to the sidebar
st.sidebar.image(pic, caption='Luna')


# importing CSS layouts for Nutrition tab
with open('Utilities/OverviewStyle_2.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write("---")


# Row A
a1, a2, a3 = st.columns(3)
a1.metric("Current Stage", "A")
a2.metric("Average Sodium Intake", "37")
a3.metric("Current Furosemide intake", "3.125")


# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Average Heart rate", "120")
b2.metric("Average Respitory Rate", "25 BpM")
b3.metric("Highest temperature", "4")
b4.metric("Lowest temperature", "5")

# with st.container():
#    st.write("This is inside the container")
#
#    # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))



#dummy data
num_days = 29  # specify the number of days to go back
start_date = (datetime.now() - timedelta(days=num_days)).strftime('%Y-%m-%d')
end_date = pd.Timestamp.now().date() + pd.Timedelta(days=1)  # add 1 day to get tomorrow's date as the end date
date_range = pd.date_range(start=start_date, end=end_date)  # create the date range
date_list = date_range.date.tolist()

sodium_intake = np.random.randint(high=55, low=40, size=31)

df = pd.DataFrame({
    'date': date_list,
    'sodium_intake': sodium_intake
})


with st.container():
    # create three columns and 3 rows
    bcol_1, bcol_2, bcol_3  = st.columns(3, gap="small")

    # Create the line chart
    fig = px.line(df, x='date', y='sodium_intake')

    # Add the threshold line
    threshold = 45
    # removing y-axis grid lines
    fig.update_yaxes(showgrid=False, showline=True)
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
        # updating the size and alignments of Line chart
        fig.update_layout(
            autosize=False,
            width=300,
            height=300,
            margin=dict(
                l=60,
                r=5,
                b=120,
                t=1,
                pad=0
            ),
     )

    # Pie chart
    st.plotly_chart(fig, use_container_width=False)

    # area chart
    st.area_chart(df_over_threshold, use_container_width=False)


    labels = ['Good', 'Bad', 'Average', 'Critical']
    values = [21, 12, 55, 2]



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
    fig.update_traces(hole=.7)
    # header of the pie chart
    bcol_2.header("Overall Health")

    bcol_2.plotly_chart(fig)