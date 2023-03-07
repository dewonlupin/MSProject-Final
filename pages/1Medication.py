

import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# creating title for the Medication page
'''
Medication and Prognosis
---
'''
st.write("---")


#extracting style sheet
with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# import OverallHealthdata.csv
path = "F:\\MS_Project\\MSProject-Final\\Utilities\\OverallHealthData.csv"
medic_data = pd.read_csv(path)


# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')


# #assigning columns for metrices
# col1, col2, col3 = st.columns(3, gap='medium')
#
# # Row A
# a1, a2, a3 = st.columns(3)
# a1.metric("Humidity", "1"+"%")
# a2.metric("Feels like", "2")
# a3.metric("Highest temperature", "4")
#
# # Row B
# b1, b2, b3, b4 = st.columns(4)
# b1.metric("Humidity", "1"+"%")
# b2.metric("Feels like", "2")
# b3.metric("Highest temperature", "4")
# b4.metric("Lowest temperature", "5")
#
#
# st.write("---")

# create on rightmost column
chart_name, *_, sel_col = st.columns(5, gap="small")

# medication data
medication = ['Enalapril', 'Pimobendan', 'Furosemide', 'Spironolactone', 'Carvedilol'] #, 'all']

chart_name.header("Medication: ")
with sel_col:
    medic_chart = st.selectbox(
        'Select the medication:', (medication)
    )



enra = medic_data[["Date", medication[0]]]
#enra = enra[enra[medication[0]] != 0]

pimo = medic_data[["Date", medication[1]]]

furo = medic_data[["Date", medication[2]]]

spino = medic_data[["Date", medication[3]]]

carve = medic_data[["Date", medication[4]]]


# draw charts for each medication separately using if
if medic_chart == medication[0]:
    chart_name.write(f' {medication[0]}')
    #enra = enra[enra[medication[0]] != 0]
    # plot chart for Enalapril
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=enra['Date'], y=enra[medication[0]], name=medication[0],
                  line = dict(color='green', width=2)))

    st.plotly_chart(fig)
    st.write("---")
    st.header("Prognosis")
    st.write("**Warning**:\n"
             "Enalapril is an ACE inhibitor used to treat congestive heart failure (CHF) "
             "in dogs by reducing the workload on the heart. However, it can lower blood "
             "pressure and cause symptoms such as weakness, fainting, or difficulty breathing. "
             "Regular kidney function tests are recommended since the medication can cause kidney damage. "
             "Enalapril can also cause vomiting, diarrhea, loss of appetite, and lethargy as side effects, "
             "which should be reported to the veterinarian. While Enalapril can be an effective medication "
             "for treating CHF in dogs, it should be used under a veterinarian's supervision to monitor the "
             "dog's response and for potential side effects or complications."
             )


elif medic_chart == medication[1]:
    chart_name.write(f' {medication[1]}')
    # plot chart for Enalapril
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=pimo['Date'], y=pimo[medication[1]], name=medication[1],
                  line = dict(color='green', width=2)))

    st.plotly_chart(fig)

    st.write("---")
    st.header("Prognosis")

    st.write("**Warning**: \n"
             "Pimobendan is a commonly used medication for treating congestive heart failure (CHF) in dogs. "
             "It works by increasing the heart's strength and improving its ability to pump blood. "
             "However, it can cause some side effects such as vomiting, diarrhea, and loss of appetite. "
             "In rare cases, it can cause more serious side effects like arrhythmias, "
             "so it's important for owners to monitor their dog's response to the medication and "
             "report any concerning symptoms to their veterinarian. Additionally, regular blood tests should be "
             "performed to monitor the dog's liver function while on the medication. Overall, "
             "Pimobendan can be an effective treatment for dogs with CHF, but should only be used under the "
             "guidance of a veterinarian.")

elif medic_chart == medication[2]:
    chart_name.write(f' {medication[2]}')

    # plot chart for Enalapril
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=furo['Date'], y=furo[medication[2]], name=medication[2],
                  line = dict(color='green', width=2)))

    st.plotly_chart(fig)

    st.write("---")
    st.header("Prognosis")

    st.write("**Warning**: \n"
             "Furosemide is a diuretic medication commonly used to treat congestive heart failure (CHF) in dogs. "
             "It works by increasing the amount of urine produced by the kidneys, which helps to reduce fluid "
             "buildup in the body and ease the workload on the heart. However, it can also cause dehydration, "
             "electrolyte imbalances, and changes in blood pressure, so the dog's hydration status and "
             "electrolyte levels should be closely monitored while on the medication. "
             "Additionally, Furosemide can cause side effects such as vomiting, diarrhea, and loss of appetite, "
             "which should be reported to the veterinarian if they occur. Overall, "
             "Furosemide can be an effective medication for managing CHF in dogs, but it should be used "
             "under the guidance of a veterinarian who can monitor the dog's response to the medication "
             "and watch for any potential side effects or complications.")


elif medic_chart == medication[3]:
    chart_name.write(f' {medication[3]}')

    # plot chart for Enalapril
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=spino['Date'], y=spino[medication[3]], name=medication[3],
                  line = dict(color='green', width=2)))

    st.plotly_chart(fig)

    st.write("---")
    st.header("Prognosis")

    st.write("**Warning**: \n"
             "Spironolactone is a diuretic medication that is often prescribed to dogs with CHF. "
             "It works by blocking the action of aldosterone, a hormone that causes the body to retain"
             " salt and water. By blocking aldosterone, Spironolactone helps the body get rid of excess fluid, "
             "which can reduce the workload on the heart and improve symptoms of CHF. "
             "However, Spironolactone can also cause side effects, such as increased thirst and urination, "
             "diarrhea, vomiting, and electrolyte imbalances. In rare cases, it can cause more serious side "
             "effects such as liver damage, low blood pressure, or anemia. Therefore, dogs taking Spironolactone "
             "should be closely monitored by a veterinarian to ensure that they are responding well to the medication "
             "and to watch for any potential side effects or complications.")

elif medic_chart == medication[4]:
    chart_name.write(f' {medication[4]}')

    # plot chart for Enalapril
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=carve['Date'], y=carve[medication[4]], name=medication[4],
                  line = dict(color='green', width=2)))

    st.plotly_chart(fig)

    st.write("---")
    st.header("Prognosis")

    st.write("**Warning**: \n"
             "Carvedilol is a beta-blocker that is sometimes used to treat CHF in dogs. "
             "It works by slowing the heart rate and reducing the workload on the heart. "
             "Like other medications used to treat CHF, Carvedilol can cause a drop in blood pressure, "
             "which may lead to weakness, fainting, or difficulty breathing. Owners should monitor their dog's "
             "blood pressure and contact their veterinarian if they notice any concerning symptoms. "
             "Carvedilol may also cause some side effects, such as vomiting, diarrhea, and lethargy. "
             "If a dog experiences any of these symptoms, the medication may need to be adjusted or discontinued. "
             "Overall, Carvedilol can be an effective medication for treating CHF in dogs, but it should be "
             "used under the guidance of a veterinarian who can monitor the dog's response to the medication and "
             "watch for any potential side effects or complications.")

elif medic_chart == "all":

    enra_all = medic_data[["Date", medication[0]]]
    enra_all = enra_all[enra_all[medication[0]] != 0]

    pimo_all = medic_data[["Date", medication[1]]]
    pimo_all = pimo_all[pimo_all[medication[1]] != 0]

    furo_all = medic_data[["Date", medication[2]]]
    furo_all = furo_all[furo_all[medication[2]] != 0]

    spino_all = medic_data[["Date", medication[3]]]
    spino_all = spino_all[spino_all[medication[3]] != 0]

    carve_all = medic_data[["Date", medication[4]]]
    crave_all = crave_all[crave_all[medication[4]] != 0]

    # plot chart for all medicine
    # basic initialization of pie chart
    fig = go.Figure()

    # adding linechart for Water
    fig.add_trace(go.Scatter(x=enra_all['Date'], y=enra_all[medication[0]], name=medication[0],
                  line = dict(color='green', width=2)))

    fig.add_trace(go.Scatter(x=pimo_all['Date'], y=pimo_all[medication[1]], name=medication[1],
                             line=dict(color='yellow', width=2)))

    fig.add_trace(go.Scatter(x=furo_all['Date'], y=furo_all[medication[2]], name=medication[2],
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=spino_all['Date'], y=spino_all[medication[3]], name=medication[3],
                             line=dict(color='blue', width=2)))

    fig.add_trace(go.Scatter(x=carve_all['Date'], y=carve_all[medication[4]], name=medication[4],
                             line=dict(color='gray', width=2)))


    st.plotly_chart(fig)