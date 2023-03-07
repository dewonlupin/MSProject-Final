import altair as alt
from vega_datasets import data
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta


# creating title for the Nutrition page
'''
Overview
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
a1.metric("Current Stage", "A")
a2.metric("Average Sodium Intake", "46")
a3.metric("Current Furosemide intake", "3.125")


# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Average Heart rate", "120")
b2.metric("Average Respitory Rate", "25 BpM")
b3.metric("Optimal Macros Ratio", "5:1:2:3")
b4.metric("Max Sodium tolerance", "49 mg")



st.write("---")



#dummy data
num_days = 30  # specify the number of days to go back
start_date = (datetime.now() - timedelta(days=num_days)).strftime('%Y-%m-%d')
end_date = pd.Timestamp.now().date() + pd.Timedelta(days=1)  # add 1 day to get tomorrow's date as the end date
date_range = pd.date_range(start=start_date, end=end_date)  # create the date range
date_list = date_range.date.tolist()

sodium_intake = np.random.randint(high=55, low=30, size=num_days+2)

df = pd.DataFrame({
    'date': date_list,
    'sodium_intake': sodium_intake
})



# Create the line chart
fig = px.line(df, x="date", y="sodium_intake")

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
fig.update_layout(yaxis_title=None)
fig.update_layout(xaxis_title=None)

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




labels = ['Good', 'Bad', 'Average', 'Critical']
values = [21, 12, 55, 2]



# basic initialization of pie chart
pie = go.Figure(
    go.Pie(
        labels=labels,
        values=values,
        hoverinfo="label+percent",textinfo="percent",
            pull=[0.025, 0.025, 0.025, 0.025]
        ))

# updating the size and alignments of Pie chart
pie.update_layout(
    showlegend= False,
    autosize=False,
    width=300,
    height=300,
    margin=dict(
        l=6,
        r=5,
        b=120,
        t=1,
        pad=0
    ),
    )
pie.update_traces(hole=.7)

#dummy data
weight = np.random.randint(high=75, low=55, size=num_days+2)
#
# df_2 = pd.DataFrame({
#     'date': date_list,
#     'Weight': monthly_weight
# })

# weight chart
# basic initialization of pie chart
weight_chart = go.Figure()

# adding linechart for Weight
weight_chart.add_trace(go.Bar(x=date_list, y=weight, name='Weight'))


weight_chart.update_yaxes(showgrid=False, showline=True)

# updating the size and alignments of Pie chart
weight_chart.update_layout(
    autosize=False,
    width=200,
    height=300,
    margin=dict(
        l=6,
        r=5,
        b=120,
        t=1,
        pad=0
    ),
    )

# bar chart for respitory rate and date
# ----------------------------
# A	10-20
# B	20-30
# C	30-40
# D	40+
# ----------------------------
# dummy data for respitory rate
resp_intake = np.random.randint(high=40, low=10, size=num_days+2)

resp_data = pd.DataFrame({
    'date': date_list,
    'resp_intake': resp_intake
})

crit_resp_rate = resp_data[resp_data['resp_intake'] >= 30]
good_resp_rate = resp_data[resp_data['resp_intake'] <= 30]
# creating bar chart
resp_chart = go.Figure()

# chart should indicate red when respitory rate is more than 30
resp_chart.add_trace(go.Bar(x=good_resp_rate['date'], y=good_resp_rate['resp_intake'], name='Good Resp Rate', marker_color = 'green'))

resp_chart.add_trace(go.Bar(x=crit_resp_rate['date'], y=crit_resp_rate['resp_intake'],name='Crit Resp Rate', marker_color = 'red'))

resp_chart.update_yaxes(showgrid=False, showline=True)

# updating the size and alignments of Pie chart
resp_chart.update_layout(
    autosize=False,
    width=300,
    height=300,
    margin=dict(
        l=60,
        r=5,
        b=120,
        t=0,
        pad=0
    ),
    )
resp_chart.update_traces(showlegend=False)

# placing all charts in a container
with st.container():
    # create 5 columns and 3 rows
    bcol_1, bcol_2, bcol_3, bcol_4, bcol_5 = st.columns(5, gap='small')

    # sodium intake chart
    bcol_1.write("Sodium Intake")
    bcol_1.plotly_chart(fig, use_container_width=False)

    # header of the pie chart
    bcol_3.write("Overall Health")
    bcol_3.plotly_chart(pie, use_container_width=False)

    # plotting the final pie chart
    bcol_5.write("Weight")
    bcol_5.plotly_chart(weight_chart, use_container_width=False)

    rowb_1, rowb_2 = st.columns([2,5])
    # plotting the final resp chart
    rowb_1.write("Resp Rate")
    rowb_1.plotly_chart(resp_chart, use_container_width=False)
    #rowb_2.plotly_chart(resp_chart, use_container_width=False)


