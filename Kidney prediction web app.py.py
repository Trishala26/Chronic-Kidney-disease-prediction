# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:09:00 2023

@author: trilo
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open(r'C:\Users\trilo\OneDrive\Desktop\Machine learning\trained_model.sav','rb'))

# creating a function for prediction

def chronic_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
      return 'The person is not chronic'
    else:
      return 'The person is chronic'
  
    
  
def main():
    
    # title for a webpage
    st.title('Chronic Kidney disease prediction web app')
    
    #getting the input data
    age=st.number_input('Age')
    bp=st.number_input('Blood Pressure')
    sg=st.number_input('Specific Gravity')
    al=st.number_input('Albumin')
    su=st.number_input('Sugar')
    rbc=st.number_input('Red Blood cells')
    pc=st.number_input('Pus cells')
    pcc=st.number_input('Pus cells clone')
    ba=st.number_input("Bacteria")
    bgr=st.number_input('Blood Glucose Random')
    sod=st.number_input('Sodium')
    pod=st.number_input('Potassium')
    wc=st.number_input('White blood cell count')
    rc=st.number_input('Red blood cell count')
    hemo=st.number_input('Hemoglobin')
    htn=st.number_input('Hypertension')
    dm=st.number_input('Diabetes mellitus')
    cad=st.number_input('Coronary artery disease')
    ane=st.number_input('Anemia')    
    
    # code for prediction
    
    diagnosis=''
    
    # creating a button for prediction
    
    if st.button('Chronic test result'):
        diagnosis = chronic_prediction([age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,sod,pod,wc,rc,hemo,htn,dm,cad,ane])
        
    st.success(diagnosis)

if __name__=="__main__":
    
    main()
    


    
    
    
    
    
    