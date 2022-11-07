"""
Created on Mon Sep 26 10:15:51 2022

@author: Navin
"""

import pickle
import streamlit as st


# loading the saved models

house_price_model = pickle.load(open('House_prediction.sav','rb'))

  # page title
st.title('HOUSE PRICE PREDICTION USING ML')

    
    # code for Prediction
 page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
        ar = st.text_input('Area')
        
with col2:
        sd = st.text_input('Sale Condition')
        
with col3:
        pf = st.text_input('Parking facility')
        
with col1:
        btc = st.text_input('Buildtype_commercial (type 0 or 1)')
        
with col2:
        bth = st.text_input('Buildtype_House (type 0 or 1)')
        
with col3:
        ua = st.text_input('Utily Available')

with col1:
        strt = st.text_input('No of Streets')
        
with col2:
        mzz = st.text_input('Mzzone')
        
with col3:
        pa = st.text_input('property Age')
        
with col1:
        sqft = st.text_input('Square Feet')
        
with col2:
        nbed = st.text_input('No of Bedroms')
        
with col3:
        nbath = st.text_input('No of Bathrooms')
        
with col1:
        nrooms = st.text_input('Total Rooms')
        
with col2:
        ppsqft = st.text_input('Price Per Sqft')
        

    
if st.button('Compute Price'):
    
    diab_prediction = house_price_model.predict([[ar,sd,pf,btc,bth,ua,strt,mzz,pa,sqft,nbed,nbath,nrooms,ppsqft]])
    st.success(f"The predicted price is {diab_prediction[0]}")
    