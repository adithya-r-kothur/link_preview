import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
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
        
    
    
        categories_ref = db.collection('users').document(st.session_state.username).collection('category')
        categories = categories_ref.stream()
    
        def disp(url):
            def get_image(url):
                r = requests.get(url)
                if r:
                    return BytesIO(r.content)


            if url:
                preview = link_preview(url)
                st.image(get_image(preview.image), caption=preview.site_name)
                st.title(preview.title)
                st.write("description:", preview.description)
            
    
            

        for category_doc in categories:
            category_name = category_doc.id
            st.write(f"\nURLs in category: {category_name}")

            urls = category_doc.to_dict().get('urls', [])
            if urls:
                for url in urls:
                    disp(url)
            else:
                st.write("No URLs found in this category.")
                
                
            
    st.write(ph)    
    choice = st.selectbox("Choose a Category",["Linkedin","Medium","Youtube","Instagram"])
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            