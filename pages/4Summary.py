import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objs as go
from plotly_calplot import calplot
import random
import pandas as pd
import numpy as np

from Utilities.SummaryHelper import CalProc
import Utilities.pdfGen as pdfGen

import datetime
np.random.seed(1)


st.title("Summary")

st.write("---")
# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')

# creating five column
col_a, col_b = st.columns(2)

# Define 4 values
values = [1, 0, -1, -2]

year = col_b.selectbox("Pick a year", ["2021", "2022", "2023"])

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
    colorscale=["green","yellow", "orange", "#990000","#001933"],     #   blackbody inferno
    gap=.3,
    month_lines_width=2,
    month_lines_color="#003366",
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
col_a.header("Overall Condition")

# plot the chart if year is present inside the data
if year in user_data["Date"][0] and year in user_data["Date"][len(user_data)-1]:
    st.caption("Condition codes are: Green = Good, yellow = Average, Orange = Bad and Red = Critical")
    st.plotly_chart(fig)


    fig.write_image("Utilities/ImageData/" + "OverallCondition" + ".png")
    if user_data["Predicted State"][len(user_data)-1] == "Good":
        st.write("Congratulations! Your dogo is doing GOOD!!")
    if user_data["Predicted State"][len(user_data)-1] == "Average":
        st.write("Dont worry! Keep it up your companion is doing Average.")
    if user_data["Predicted State"][len(user_data)-1] == "Bad":
        st.write("Attention!! if your dog's symptoms doesnt recovers then talk to vet hospital.")
    if user_data["Predicted State"][len(user_data)-1] == "Critical":
        st.error("Please contact Veterinary Center ASAP!! ")
        st.warning("For previous references please click generate PDF under 'Report' section.")


st.write("---")
st.header("Report")

med_col, symp_col_a = st.columns(2)

medications = user_data["Date"][len(user_data) - 1]

med_col.subheader("**Medications**")

with med_col:
    st.write("Enalapril"      + " Dossage :     ", user_data["Enalapril"][len(user_data)-1])
    st.write("Furosemide"     + " Dossage :     ", user_data["Furosemide"][len(user_data)-1])
    st.write("Spironolactone" + " Dossage :     ", user_data["Spironolactone"][len(user_data)-1])
    st.write("Pimobendan"     + " Dossage :     ", user_data["Pimobendan"][len(user_data)-1])


symp_col_a.subheader("Symptoms")
symp_col = user_data.columns[1:9]

symptoms_for_pdf = []

for symptoms in symp_col:
  if user_data[symptoms][len(user_data) - 1] == 1:
     symp_col_a.write(symptoms)
     symptoms_for_pdf.append(symptoms)


st.write("---")
if user_data["Predicted State"][len(user_data)-1] == "Good":
    st.subheader("Overall condition for" + user_data["Date"][len(user_data)-1] + ": Good")
if user_data["Predicted State"][len(user_data)-1] == "Average":
    st.subheader("Overall condition for" + user_data["Date"][len(user_data)-1] + ": Average")
if user_data["Predicted State"][len(user_data)-1] == "Bad":
    st.subheader("Overall condition for" + user_data["Date"][len(user_data)-1] + ": Bad")
if user_data["Predicted State"][len(user_data)-1] == "Critical":
    st.subheader("Overall condition for " + user_data["Date"][len(user_data)-1] + ": Critical")


st.write("---")
_, pdf_gen, _ = st.columns(3)

medication_for_pdf = ['Enalapril', 'Pimobendan', 'Furosemide', 'Spironolactone']
latest_data = user_data.iloc[len(user_data) - 1]

# pass these data to generate pdf
# symptoms_for_pdf, medicaiton_for_pdf and latest_data

pdfGen.pdf_generator(latest_data, symptoms_for_pdf, medication_for_pdf)

with open("Report.pdf", "rb") as file:
    pdfFile = file.read()

pdf_gen.download_button(
    label="Generate PDF",
    data=pdfFile,
    file_name="Report.pdf",
    mime='application/octet-stream'
)