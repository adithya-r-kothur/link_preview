import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore

def app():        
    st.title("Welcome to Home") 
    