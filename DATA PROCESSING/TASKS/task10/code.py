import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\shahd\\Desktop\\depi\\CA-R5-AIS2-S1\\DATA PROCESSING\\TASKS\\task10\\insurance.csv")
#check null values
checknull=df.isnull().sum()
print("null =\n",checknull)

#describe data
print("describe =\n",df.describe())

#duplicated values
duplicated=df.duplicated().sum()
print("duplicated = ",duplicated)

#check unique values
df.drop_duplicates(keep='first', inplace=True)
print("unique values =\n",df['sex'].unique())
print("unique values =\n",df['smoker'].unique())
print("unique values =\n",df['region'].unique())

#encoding
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['region']=df['region'].map({'southeast':0, 'southwest':1, 'northeast':2, 'northwest':3})

#handle outliers
Q1 = df['bmi'].quantile(0.25)
Q3 = df['bmi'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df['bmi']=df['bmi'].clip(lower=lower, upper=upper)

Q1_ch = df['charges'].quantile(0.25)
Q3_ch = df['charges'].quantile(0.75)
IQR_ch = Q3_ch - Q1_ch
lower_ch = Q1_ch - 1.5 * IQR_ch
upper_ch = Q3_ch + 1.5 * IQR_ch
df['charges']=df['charges'].clip(lower=lower_ch, upper=upper_ch)

print(df.head())