
import streamlit as st 
import numpy as np

import pickle

st.set_page_config(layout='wide')
st.title("Intrusion Detection System")

col1, col2, col3 , col4 , col5 = st.columns([1,1,2,1,1]) 



with col1:
    a = st.number_input('Destination Port' , step=0) 
    b = st.number_input('Total Backward Packets') 
    c = st.number_input('Total Length of Fwd Packets') 
    d = st.number_input('Fwd Packet Length Max') 
    e = st.number_input('Fwd Packet Length Mean') 
    f= st.number_input('Bwd Packet Length Max ') 
with col2:
    g = st.number_input('Bwd Packet Length Mean') 

    h = st.number_input(' Bwd Packet Length Std') 
    i = st.number_input('Flow IAT Min')
    j = st.number_input('Fwd IAT Mean')
    k = st.number_input('Fwd IAT Min')
    l = st.number_input('Bwd IAT Std')
with col3:
    m = st.number_input('Bwd IAT Min')
    n = st.number_input('Fwd Header Length')
    o = st.number_input('Bwd Packets/s')
    p = st.number_input('Packet Length Mean')
    q = st.number_input('Packet Length Variance')
    r = st.number_input('PSH Flag Count')

with col4:
    s = st.number_input('URG Flag Count')
    t = st.number_input('Down/Up Ratio')
    u = st.number_input('Average Packet Size')
    v = st.number_input('Avg Bwd Segment Size')
    w = st.number_input('Fwd Header Length.1')
    x = st.number_input('Subflow Fwd Packets')

with col5:
    y = st.number_input('Init_Win_bytes_forward')
    z = st.number_input('Init_Win_bytes_backward')
    ha = st.number_input('min_seg_size_forward')
    mz = st.number_input('Active Std')
  




				



with col5:
    


    model = pickle.load(open('rfcmodel.pkl', 'rb'))
    accuracy = 99.80



submit_button = st.button(label='Predict')
# Make predictions based on user inputs and selected model
attacks = ['Bengin', 'Bot', 'Brute Force', 'DoS' ,'DDoS', 'Ports scan', 'Web Attack']
if submit_button:
    prediction = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,ha,mz]])
    st.write(f"The prediction result is ", f"'{attacks[prediction[0]]}'" , f"with accuracy of {accuracy}% ")
show = st.button(label=f"more about Random Forrest? ")

if show:



    with col1: 
        st.image('rfccm.png', caption="Confusin Matrix" , width=500)
    with col3:
        st.image('featureimportance.png', caption="feature importance" , width=600)