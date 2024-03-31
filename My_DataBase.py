import streamlit as st
from firebase_admin import firestore


def app():
    st.write('My_DataBase')
    
    if 'db' not in st.session_state:
        st.session_state.db = ''
        
    db=firestore.client()  
    st.session_state.db=db  
    
    ph = ''
    if st.session_state.username=='':
        ph = 'Login to be able to see your contetnt!!'
    else:
        ph='Enjoy your content'
        
    st.write(ph)    