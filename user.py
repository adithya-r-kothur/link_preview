import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore

def app():        
    if 'db' not in st.session_state:
        st.session_state.db = ''
        
    db=firestore.client()  
    st.session_state.db=db  
    
    ph = ''
    if st.session_state.username=='':
        ph = 'Login to be able to post!!'
    else:
        ph='Post your thought'
        
    st.write(ph)    

    category  = st.text_input("Enter the category")
    category = category.lower()
    url = st.text_input("Enter the url")
    submit = st.button("Submit")

    if url and submit:
        info = db.collection('users').document(st.session_state.username).get()
        print(info.exists)
        
        if info.exists:
                info = db.collection('users').document(st.session_state.username).collection('category').document(category)
                info1 = info.get()
                if not info1.exists:
                    info.set({
                        'urls':[url]
                    })
                else:    
                    info = info1.to_dict()
                    print(info.keys())
                    if 'urls' in info.keys():
                        print("here")
                        user=db.collection('users').document(st.session_state.username).collection('category').document(category)
                        user.update({'urls': firestore.ArrayUnion([url])})
                    
                    else:
                    
                        data={"urls":[url],'Username':st.session_state.username}
                        db.collection('users').document(st.session_state.username).collection('category').document(category).set(data)    
        
        else:
                    
                data={"urls":[url],'Username':st.session_state.username}
                db.collection('users').document(st.session_state.username).collection(category).document(category).set(data)
                
        st.success('Post uploaded!!')    