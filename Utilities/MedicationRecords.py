'''
------------------------------------------------------------------------------------------ Medication Dummy DataFrame ------------------------------------------------------------------------------------------


#   Medication	                Dosage-Range	                         Category	    Stage-A	                            Stage-B	                            Stage-C	                                        Stage-D
# Furosemide	        1-2 mg/kg orally every 8-12 hours	             Diuretic	       -	                                -	                            2-4 mg/kg every 8-12 hours	                4-6 mg/kg every 8-12 hours
# Spironolactone	    1-2 mg/kg orally every 12-24 hours	             Diuretic	       -	                                -	                            1-2 mg/kg every 12-24 hours	                1-2 mg/kg every 12-24 hours
# Hydrochlorothiazide	1-2 mg/kg orally every 12-24 hours	             Diuretic	       -	                                -	                            1-2 mg/kg every 12-24 hours	                1-2 mg/kg every 12-24 hours
# Enalapril	            0.25-0.5 mg/kg orally every 12-24 hours	ACE      inhibitor	    0.25-0.5 mg/kg every 12-24 hours    0.25-0.5 mg/kg every 12-24 hours	0.25-0.5 mg/kg every 12-24 hours	                -
# Benazepril	        0.25-0.5 mg/kg orally every 12-24 hours	ACE      inhibitor	    0.25-0.5 mg/kg every 12-24 hours	0.25-0.5 mg/kg every 12-24 hours	0.25-0.5 mg/kg every 12-24 hours	                -
# Carvedilol	        0.1-0.2 mg/kg orally every 12 hours	             Beta-blocker	   -	                            0.1-0.2 mg/kg every 12 hours	    0.1-0.2 mg/kg every 12 hours	                    -
# Atenolol	            0.5-1 mg/kg orally every 12-24 hours	         Beta-blocker	   -	                            0.5-1 mg/kg every 12-24 hours	    0.5-1 mg/kg every 12-24 hours	                    -
# Digoxin	            0.0025-0.005 mg/kg orally every 12-24 hours	     Digoxin	       -	                                -	                            0.0025-0.005 mg/kg every 12-24 hours	    0.0025-0.005 mg/kg every 12-24 hours
# Pimobendan	        0.2-0.5 mg/kg orally every 12 hours	             Inodilator	       -	                                -	                            0.2-0.5 mg/kg every 12 hours	            0.2-0.5 mg/kg every 12 hours

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


import numpy as np
import pandas as pd
import datetime


def probability_populator(data_f, df_stage, probab, symp):
    for i in data_f.index:
        if data_f['Stage'][i] == df_stage:
            size = len(data_f[data_f['Stage'] == df_stage])
            var = np.random.binomial(1, probab / 5, size=size)
            k = 0
            for j in range(i, size + i):
                data_f[symp][j] = var[k]
                k = k + 1

    return data_f


# Define the probability of each symptom occurring at each stage of CHF
cough = [0.1, 0.2, 0.5, 0.8]                    #cough[0:-1]
difficulty_breathing = [0.1, 0.3, 0.6, 0.9]
tiring_easily = [0.1, 0.2, 0.4, 0.7]
swelling = [0.1, 0.3, 0.7, 0.9]
loss_of_appetite = [0.1, 0.3, 0.6, 0.9]
weight_gain = [0.1, 0.2, 0.5, 0.8]
restlessness = [0.1, 0.3, 0.6, 0.9]
pacing = [0.1, 0.3, 0.7, 0.9]

# Define the guidelines for dosage for each medication at each stage of CHF
dosage_guidelines = {
    'Stage A': {'Enalapril': 1, 'Pimobendan': 0, 'Furosemide': 0, 'Spironolactone': 0, 'Carvedilol': 0},
    'Stage B': {'Enalapril': 1, 'Pimobendan': 1, 'Furosemide': 0.5, 'Spironolactone': 0, 'Carvedilol': 0},
    'Stage C': {'Enalapril': 2, 'Pimobendan': 1, 'Furosemide': 1, 'Spironolactone': 1, 'Carvedilol': 1},
    'Stage D': {'Enalapril': 2, 'Pimobendan': 2, 'Furosemide': 2, 'Spironolactone': 2, 'Carvedilol': 2}
}




medications = ['Furosemide', 'Enalapril', 'Pimobendan', 'Spironolactone', 'Carvedilol']
dosages = {
    'Furosemide': [0.5, 2, 2, 8, 4, 12, 6, 20],
    'Enalapril': [0.25, 0.5, 0.5, 1, 1, 2, 1.5, 2.5],
    'Pimobendan': [0.125, 0.25, 0.25, 0.5, 0.5, 1, 0.75, 1.25],
    'Spironolactone': [0.25, 1, 1, 4, 2, 6, 3, 10],
    'Carvedilol': [2.5, 6.25, 6.25, 12.5, 12.5, 25, 25, 50]
}

data = []
start_date = datetime.date(2020, 11, 21)

for i in range(300):
    stage = 'A' if i < 75 else 'B' if i < 150 else 'C' if i < 225 else 'D'
    for medication in medications:
        dosage = dosages[medication][2*(ord(stage)-65):2*(ord(stage)-63)]
        if len(dosage) > 0:
            if np.isnan(dosage[0]):
                dosage_str = '-'
            else:
                if len(dosage) == 1:
                    dosage_str = f'{dosage[0]:.3f}'
                else:
                    dosage_str = f'{np.mean(dosage):.3f}'
        else:
            dosage_str = '-'
        category = 'Diuretic' if medication in ['Furosemide', 'Spironolactone'] \
            else 'ACE inhibitor' if medication in ['Enalapril'] \
            else 'Beta-blocker' if medication == 'Carvedilol' \
            else 'Inodilator' if medication == 'Pimobendan' \
            else 'Positive inotrope'

        data.append([start_date + datetime.timedelta(days=i), medication, category, dosage_str, stage])


df = pd.DataFrame(data, columns=['Date', 'Medication', 'Category', 'Dosage', 'Stage'])


df['Condition'] = df['Stage']
df['NCondition'] = df['Condition']


for i in df.index:
  if df['Stage'][i] == 'A':
    df['Condition'][i] = 'Good'
    df['NCondition'][i] = 1

  elif df['Stage'][i] == 'B':
    df['Condition'][i] = 'Average'
    df['NCondition'][i] = 0

  elif df['Stage'][i] == 'C':
    df['Condition'][i] = 'Bad'
    df['NCondition'][i] = -1

  elif df['Stage'][i] == 'D':
    df['Condition'][i] = 'Critical'
    df['NCondition'][i] = -2

medic_record = df

medic_record['cough'] = df['Stage']
medic_record['difficulty_breathing'] =df['Stage']
medic_record['tiring_easily'] =df['Stage']
medic_record['swelling'] =df['Stage']
medic_record['loss_of_appetite'] =df['Stage']
medic_record['weight_gain'] =df['Stage']
medic_record['restlessness'] =df['Stage']
medic_record['pacing'] =df['Stage']

stage = ["A", "B", "C", "D"]


for i in range(0,len(cough)):
  draft = probability_populator(medic_record, stage[i], cough[i], 'cough')
  draft = probability_populator(draft, stage[i], difficulty_breathing[i], 'difficulty_breathing')
  draft = probability_populator(draft, stage[i], tiring_easily[i], 'tiring_easily')
  draft = probability_populator(draft, stage[i], swelling[i], 'swelling')
  draft = probability_populator(draft, stage[i], loss_of_appetite[i], 'loss_of_appetite')
  draft = probability_populator(draft, stage[i], weight_gain[i], 'weight_gain')
  draft = probability_populator(draft, stage[i], restlessness[i], 'restlessness')
  draft = probability_populator(draft, stage[i], pacing[i], 'pacing')



'''
-----------------------------------------------------------------------------------------------------------------
------------------------------- Things can be done after applying ML in this data -------------------------------
-----------------------------------------------------------------------------------------------------------------

1. Predicting the likelihood of developing CHF: By analyzing patterns in the data, the model could potentially 
    identify factors that increase a dog's risk of developing CHF, such as breed, age, and underlying health 
    conditions. This information could be used by veterinarians to monitor at-risk dogs more closely and take 
    preventative measures to slow the progression of the disease.

2. Personalized treatment plans: The model could potentially suggest personalized treatment plans based on a 
    dog's specific characteristics and medical history. For example, the model could recommend a specific 
    medication or dosage based on the dog's age, breed, and symptom severity. This could lead to more effective 
    treatment and improved quality of life for dogs with CHF.

3. Identifying new risk factors or treatment options: By analyzing the data, the model may be able to identify new 
    risk factors or treatment options that have not yet been discovered. For example, the model may uncover a 
    previously unknown link between a certain breed and CHF, or suggest a new medication that has not yet been 
    tested for CHF.

4. Early detection and intervention: The model could potentially detect early warning signs of CHF before symptoms
   become severe. This could allow for earlier intervention and treatment, which may improve outcomes and quality 
   of life for affected dogs.

5. Monitoring disease progression: The model could potentially track changes in a dog's condition over time and 
   provide insights into how the disease is progressing. This could allow veterinarians to adjust treatment plans 
   as needed and provide more targeted care.
-----------------------------------------------------------------------------------------------------------------
'''