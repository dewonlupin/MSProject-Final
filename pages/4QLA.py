
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np
import os

from Utilities.ConditionClassifier import condition_classifier

'''
Quality Of Life Assessment
---------------------------------
---------------------------------
'''
# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')


col1, clo2, col3 = st.columns(3, gap="small")

date = col3.date_input("Select today's date for the record")
if date > date.today():
    col3.error("Please select date prior to today's date.")

col1.write("this page is for your dog's overall health assessment.")
col1.write("Please fill in the given form given bellow to get health assessment.")

'''
1. Medication:
'''
medic = []

x = st.text_input("a. How often do you give your dog Furosemide? (write 0 if its not prescribed)")
# text input
medic.append(x)

x = st.text_input("b. What is the dosage of Pimobendan prescribed for your dog? (write 0 if its not prescribed)")
# text input
medic.append(x)

x = st.text_input("c. What is the dosage of Enalapril prescribed for your dog? (write 0 if its not prescribed)")
# text input
medic.append(x)

x = st.text_input("d. What is the dosage of Spironolactone prescribed for your dog? (write 0 if its not prescribed)")
# text input
medic.append(x)

x = st.text_input("e. What is the dosage of Carvedilol prescribed for your dog? (write 0 if its not prescribed)")
# text input
medic.append(x)


'''
2. Symptoms:
'''

symp =[]

# cough --> difficulty in breathin --> tiring easily --> swelling --> loss of apetite --> weight gain --> restlessness --> pacing -->
y = st.text_input("a. Is your dog coughing regularly?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("b. Is your dog difficulty in breathing regularly?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("c. Is your dog tiring easily regularly?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("d. Does your dog have swelling in his/her body?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("e. Does your dog have loss of appetite?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("f. Does your dog have gained weight?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("g. Is your dog acting restlessnessly?(1:Yes/0:No)")
# text input
medic.append(y)

y = st.text_input("h. Does your dog pacing regularly?(1:Yes/0:No)")
# text input
medic.append(y)



stage = st.text_input("What is the current stage of your dog?(A:1, B:0, C:-1, D:-2)")

# collect all list and pass it to the function like this
# ==> condition_classifier(medic, stage) where,
# 1. medic[0:4] = Medication
# 2. medic[5:12] = Symptoms
# 3. stage = Current stage of CHF in dog
# function will return a string that will classify current condition
# of dog into ['Good','Average','Bad','Critical']

checkbox_val = st.checkbox("by checking the box you are agreeing to our terms and conditions")

checkbox_store = st.checkbox("If you need to store this entry then please click here")


_,_, c1, c2, *_ = st.columns(6)
# Every form must have a submit button.
submitted = c1.button("Submit")
reset = c2.button("Reset")


# TODO: check why the if condition is not getting in

# checking if submitted button is pushed and medic only contains 0s and 1s
if submitted and checkbox_val:
    st.success("Your form has been submitted please check Summary page!")
    current_state = condition_classifier(date, medic, stage)
    st.write("Current state of your dog: ", current_state)


# performs a page reset
if reset:
    # resets the whole form
    st.write("reset has been triggered")
    st.experimental_rerun()

if submitted and checkbox_val and checkbox_store:
    st.write("You selected to store the value")
    # create a dataframe
    medication = medic[5:13]

    data = {"Date":date, "cough":medication[0], "difficulty_breathing": medication[1], "tiring_easily":medication[2],
            "swelling":medication[3], "loss_of_appetite":medication[4], "weight_gain":medication[5],
            "restlessness":medication[6], "pacing":medication[7], "Enalapril":medic[0],
            "Pimobendan":medic[1] ,"Furosemide":medic[2], "Spironolactone":medic[3], "Stage":stage,
            "Predicted State":current_state}

    # enter the value from medic into dataframe
    # if file exists
    file_path = "F:\\MS_Project\\MSProject-Final\\Utilities\\user_data.csv"
    if os.path.exists(file_path):
        df_in = pd.read_csv(file_path)
        # newly generated data
        new_data = pd.DataFrame(data, index=[0])
        # Append new data to existing dataframe
        df_in = pd.concat([df_in, new_data], ignore_index=True)
        # Write updated dataframe back to CSV file
        df_in.to_csv(file_path, index=False)
        st.write(df_in)

    else:
        df_in = pd.DataFrame(data, index=[0])
        # convert dataframe into csv
        df_in.to_csv(file_path, index=False)


