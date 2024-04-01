from bs4 import BeautifulSoup
import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore

def gen(url):

    def get_img(url):
            r = requests.get(url)
            return BytesIO(r.content)

    def generate_preview(url):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        # url = request.GET.get('link')
        # print(url)
        req = requests.get(url, headers)
        html = BeautifulSoup(req.content, 'html.parser')
        meta_data = {
            'title': get_title(html),
            'description': get_description(html),
            'image': get_image(html),
        }

        print(meta_data)
        
        st.image(get_img(get_image(html)))
        st.title(get_title(html))
        st.write(get_description(html))


    def get_title(html):
        """Scrape page title."""
        title = None
        if html.title.string:
            title = html.title.string
        elif html.find("meta", property="og:title"):
            title = html.find("meta", property="og:title").get('content')
        elif html.find("meta", property="twitter:title"):
            title = html.find("meta", property="twitter:title").get('content')
        elif html.find("h1"):
            title = html.find("h1").string
        return title


    def get_description(html):
        """Scrape page description."""
        description = None
        if html.find("meta", property="description"):
            description = html.find("meta", property="description").get('content')
        elif html.find("meta", property="og:description"):
            description = html.find(
                "meta", property="og:description").get('content')
        elif html.find("meta", property="twitter:description"):
            description = html.find(
                "meta", property="twitter:description").get('content')
        elif html.find("p"):
            description = html.find("p").contents
        return description


    def get_image(html):
        """Scrape share image."""
        image = None
        if html.find("meta", property="image"):
            image = html.find("meta", property="image").get('content')
        elif html.find("meta", property="og:image"):
            image = html.find("meta", property="og:image").get('content')
        elif html.find("meta", property="twitter:image"):
            image = html.find("meta", property="twitter:image").get('content')
        elif html.find("img", src=True):
            image = html.find_all("img").get('src')
        return image


    generate_preview(url)


def app():
    st.write('My_DataBase')
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    
    if 'db' not in st.session_state:
        st.session_state.db = ''
        
    db=firestore.client()  
    st.session_state.db=db  
    
    ph = ''
    if st.session_state.username=='':
        st.write('Login to be able to see your contetnt!!')
    else:
        st.write('Enjoy your content')
        
    
        
        categories_ref = db.collection('users').document(st.session_state.username).collection('category')
        categories = [doc.id for doc in categories_ref.stream()]

        st.title("User Categories and URLs")

        if categories:
            selected_category = st.selectbox("Select a Category:", categories)

            urls_ref = db.collection('users').document(st.session_state.username).collection('category').document(selected_category)
            urls_doc = urls_ref.get()
            
            if urls_doc.exists:
                urls = urls_doc.to_dict().get('urls', [])
                st.write("URLs in this category:")

                for index, url in enumerate(urls):
                    gen(url)
                    st.write(f"{index + 1}. {url}")  # Number the URLs
                    if st.button(f"Delete URL {index + 1}", key=index): 
                        del urls[index]  # Remove from the list
                        urls_ref.update({'urls': urls})  # Update Firestore
                        st.experimental_rerun()  # Refresh the UI
                    st.divider()    
            else:
                st.write("No URLs found in this category.") 
        else:
            st.write("No categories found for this user.")
                
            

    
    
    
    
    
    
    
    
    
    
            
            
            
            