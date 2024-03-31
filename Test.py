import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore


def app():

    st.write("Home")
    st.title("Link Preview Generator")


    st.write("Enter a Link")
        
    url = st.text_input("Enter the URL of the link you want to preview")

    def get_image(url):
        r = requests.get(url)
        return BytesIO(r.content)


    if url:
        preview = link_preview(url)
        st.image(get_image(preview.image), caption=preview.site_name)
        st.title(preview.title)
        st.write("description:", preview.description)
        
    else:
        st.write("Looks like you have'nt Entered a URL to preview")