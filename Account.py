import streamlit as st
import firebase_admin 

from firebase_admin import credentials
from firebase_admin import auth
import streamlit as st
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

import user as customer

cred = credentials.Certificate("link-preview-gen.json")
try:
    firebase_admin.get_app()
except ValueError as e:
    firebase_admin.initialize_app(cred)

def app():
    st.title("Create An Account OR Login")
    
    db=firestore.client()  
    st.session_state.db=db
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
        
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
          
    def f():
        try:
            user = auth.get_user_by_email(email)
            st.success("login successful")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signout = True
            st.session_state.signedout = True
        except:
            st.warning("User Not Found")
            
            
    def t():
        st.session_state.signedout = False
        st.session_state.signout = False
        st.session_state.username = ''
        st.session_state.useremail = ''
        st.success("Signed Out Successfully")        

            
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
        
    if 'signout' not in st.session_state:
        st.session_state.signout = False 
        
        
    if not st.session_state['signedout']:            
        choice = st.selectbox("SignUp/Login",["SignUp","Login"])    
            

        if choice == 'Login':
            email = st.text_input("Enter Your Email Address")
            password = st.text_input("Enter Your Password",type='password')
            st.button("Login",on_click=f)
            
        else:
            email = st.text_input("Enter Your Email Address")
            password = st.text_input("Enter Your Password", type='password')
            username = st.text_input("Enter Your Username")
            
            if st.button("Create Account") and email and password and username:
                user = auth.create_user(
                    email=email,
                    password=password,
                    uid=username
                )
                data={'Username':username}
                db.collection('users').document(username).set(data)
                
                st.success("Account Created Successfully")
                st.markdown("Login To Continue")
                
                
                
                
                
    if st.session_state.signout:
        # st.text('Name:'+st.session_state.username)
        # st.text('Email:'+st.session_state.useremail)
        customer.app()     
        st.button("Signout",on_click=t) 