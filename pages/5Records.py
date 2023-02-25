import streamlit as st
import time
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np


# Create the sidebar
st.sidebar.title("CHF DashBoard")


pic = Image.open('Utilities/logo.jpg')
st.sidebar.image(pic, caption='Luna')

report_df = pd.DataFrame()
'''
---------------------------------
Reports
---------------------------------
'''

col1, clo2, col3 = st.columns(3)

date = col3.date_input('Select date for your report')
col3.write(date)


'''
1. Medication:
'''
medic = []

x = st.text_input("How often do you give your dog Furosemide?")
# text input
medic.append(x)

x = st.text_input("What is the dosage of Pimobendan prescribed for your dog?")
# text input
medic.append(x)

x = st.text_input("Has your dog been prescribed any other medications for CHF?")
# text input
medic.append(x)

if len(medic) == 3:
    st.success("Success entered 'Medication'")
else:
    st.error("Error in entering 'Medication'")

st.text(medic)


'''
2. Prognosis:
'''
prog = []

x = st.text_input("Has your dog had any recent changes in exercise tolerance?")
# text input
prog.append(x)

x = st.text_input("Has your dog had any recent episodes of coughing or difficulty breathing?")
# text input
prog.append(x)

x = st.text_input("Have there been any changes in your dog's appetite or weight?")
# text input
prog.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Prognosis'")
else:
    st.success("Success entered 'Prognosis'")


'''
3. Daily activity:
'''
dac =[]

x = st.text_input("How often does your dog go for a walk?")
# text input
dac.append(x)

x = st.text_input("How long is each walk?")
# text input
dac.append(x)

x = st.text_input("What is your dog's usual level of physical activity during the day?")
# text input
dac.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Daily-activity'")
else:
    st.success("Success entered 'Daily-activity'")


''' 
4. Calories intake:
'''
calin = []

x = st.text_input("What type of food does your dog eat?")
# text input
calin.append(x)

x = st.text_input("How often do you feed your dog?")
# text input
calin.append(x)

x = st.text_input("What is the estimated calorie intake per day for your dog?")
# text input
calin.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Calories-intake'")
else:
    st.success("Success entered 'Calories-intake'")


'''
5. Supplement intake:
'''
supin = []
x = st.text_input("Is your dog currently taking any supplements?")
# text input
supin.append(x)

x = st.text_input("What supplements is your dog taking?")
# text input
supin.append(x)

x = st.text_input("How often does your dog take these supplements?")
# text input
supin.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Supplement-intake'")
else:
    st.success("Success entered 'Supplement-intake'")


'''
6. Water intake:
'''
water =[]

x = st.text_input("How much water does your dog drink per day?")
# text input
water.append(x)

x = st.text_input("Is your dog showing any signs of increased thirst or urination?")
# text input
water.append(x)

x = st.text_input("Have there been any changes in your dog's water intake recently?")
# text input
water.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Water intake'")
else:
    st.success("Success entered 'Water intake'")


'''
7. Calories burned:
'''
calout = []

x = st.text_input("How many calories does your dog burn per day?")
# text input
calout.append(x)

x = st.text_input("What is the level of physical activity that your dog engages in during the day?")
# text input
calout.append(x)

x = st.text_input("Are there any changes in your dog's daily activity level recently?")
# text input
calout.append(x)

if len(medic) < 3:
    st.error("Error in entering 'Calories burned'")
else:
    st.success("Success entered 'Calories burned'")


pic = st.camera_input("Take a picture")

st.button('Click me')

st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
#st.download_button('Download file', data)
#st.camera_input("Take a picture")
st.color_picker('Pick a color')


col1, col2 = st.columns(2)



with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')


