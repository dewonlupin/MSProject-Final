
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np

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

date = col3.date_input('Select todays date for the record')
col3.write(date)

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

_,_, c1, c2, *_ = st.columns(6)
# Every form must have a submit button.
submitted = c1.button("Submit")
reset = c2.button("Reset")

if submitted:
    #st.write(date, medic, stage)
    current_state = condition_classifier(date, medic, stage)

if reset:
    # resets the whole form
    st.experimental_rerun()
    st.write("reset has been triggered")