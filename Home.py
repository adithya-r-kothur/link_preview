import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore

def app():   
    
    st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
    )      
    st.title("Welcome to Home") 
    