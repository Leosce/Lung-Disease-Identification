import streamlit as st
from keras.models import load_model
from PIL import Image
import cv2 
import numpy as np
from classify import classify

st.title('Lung Disease Classification')

st.header('Please upload a chest X-ray.')

file = st.file_uploader('', type=['jpg','jpeg','png'])

model=load_model(".\\models\\lung_disease_identification.h5")

class_names=['COVID-19','Normal','Viral Pneumonia']

if file is not None:
    image = Image.open(file)
    
    st.image(image, use_container_width=True)
    st.write('# {}'.format('Prediction for each class: '))
    
    yhat, pred=classify(image,model)
    pred_class = 'COVID-19' if pred==0 else 'Normal' if pred==1 else 'Viral Pneumonia'
    
    for i in range(len(yhat[0])): 
        
        conf = f"{yhat[0][i] * 100:.2f}"
        conf = str(conf)
        
        st.write('## {}'.format(class_names[i]+':&nbsp;&nbsp;'+conf+'%'))

    
    st.write('# Predicted Class is: {}'.format(pred_class))