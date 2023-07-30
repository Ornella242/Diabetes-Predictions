import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

pickle_in = open('randomforestclassifier.pkl', 'rb')
model = pickle.load(pickle_in)

st.title("Diabetes predictions for pregnant woman")
st.write("Developed by Africa Agility cohort 6")

### Inputing Variables
name = st.text_input("Name of the individual")
Pregnancies   = st.number_input("No of times being pregnant: ")           
Glucose       = st.number_input("Amount of Glucose: ") 
BloodPressure = st.number_input("BloodPressure: ")     
SkinThickness = st.number_input("SkinThickness: ") 
Insulin       = st.number_input("Insulin: ") 
BMI           = st.number_input("BMI: ") 
DiabetesPedigreeFunction  = st.number_input("DiabetesPedigreeFunction: ") 
Age   = st.number_input("Age: ")  

button = st.button("Predict")

### make predictions
if button:
    predictions = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,]]) 
if predictions == 0:
    st.write("Oooooooooooooops",name,"is diabetic")
else:
    st.write(name,"is not diabetic")