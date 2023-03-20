
import pandas as pd
import pickle
import streamlit as st
import numpy as np


# to decode the output into ['Good','Average','Bad','Critical']
def decode_condition(predicted_value):
    if predicted_value == 1:
        return 'Good'
    elif predicted_value == 0:
        return 'Average'
    elif predicted_value == -1:
        return 'Bad'
    elif predicted_value == -2:
        return 'Critical'
    else:
        return 'Unknown'


# value organizer function:
def val_organizer(medic, stage):
    # second append in for loop
    medication = medic[0:5]


    # first append in for loop
    symptoms = medic[5:13]
    conv_stage =[]
    # convert int stage into bits (A:1, B:0, C:-1, D:-2)
    # if stage is A
    if stage == '1':
        conv_stage =[1, 0, 0, 0]

    # if stage is B
    elif stage == '0':
        conv_stage =[0, 1, 0, 0]

    # if stage is C
    elif stage == '-1':
        conv_stage = [0, 0, 1, 0]

    # if stage is D
    elif stage == '-2':
        conv_stage = [0, 0, 0, 1]

    org_val = []

    # append symptoms to org_val
    for i in symptoms: org_val.append(i)

    # append medic to org_val
    for i in medication: org_val.append(i)

    # append conv_stage to org_val
    for i in conv_stage: org_val.append(i)

    org_val = np.array(org_val)
    org_val = org_val.reshape(1, -1)

    return org_val


# Entry point of the ML model
# condition_classifier(medic, stage) where,
# 1. medic[0:7] = Symptoms
# 2. medic[8:12] = Medication
# 3. stage_bits[13:16] = Current stage of CHF in dog
# # a. Stage A = 1,0,0,0
# # b. Stage B = 0,1,0,0
# # c. Stage C = 0,0,1,0
# # d. Stage D = 0,0,0,1
# function will return a string that will classify current condition
# of dog into ['Good','Average','Bad','Critical']
def condition_classifier(date, medic, stage):

    # import the trained model from Google Colab
    filename = 'Utilities/condition_classifier.sav'
    # load the model from disk
    cond_class_model = pickle.load(open(filename, 'rb'))

    # organize the values according to the model input
    in_value = val_organizer(medic, stage)

    # store the predicted value from the imported model
    current_state_value = cond_class_model.predict(in_value)

    # decode the current state value
    current_state = decode_condition(current_state_value)

    return current_state


# create and train Random Forest Classifier to predict the Overall condition
# of patent, provided by Stage, Symptoms and Medication as input.
def ml_model():
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    # import dataframe

    # target
    y = draft['NCondition']

    # input
    col = draft.columns
    col_not_in_need = col[0:3]

    X = draft.drop(col_not_in_need, axis=1)
    X = X.drop(['Category', 'Condition', 'NCondition', 'Dosage'], axis=1)

    model = RandomForestClassifier()

    model.fit(X, y)

    '''
    ['cough', 'difficulty_breathing', 'tiring_easily', 'swelling',
           'loss_of_appetite', 'weight_gain', 'restlessness', 'pacing',
           'Enalapril', 'Pimobendan', 'Furosemide', 'Spironolactone', 'Carvedilol',
           'Stage_A', 'Stage_B', 'Stage_C', 'Stage_D']
    '''
    # [[0,0,0,0,0,0,0,0, 2,1,13,6.5,37.5, 1,0,0,0]] ==> Critical

    # Custom test data
    new_data = [[0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 13, 6.5, 37.5, 1, 0, 0, 0]]
    prediction = decode_condition(model.predict(new_data))