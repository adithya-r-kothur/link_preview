import streamlit as st
from linkpreview import link_preview
from io import BytesIO
import requests
from firebase_admin import firestore
from bs4 import BeautifulSoup


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
        print(url)
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

    st.write("Home")
    st.title("Link Preview Generator")


    st.write("Enter a Link")
        
    url = st.text_input("Enter the URL of the link you want to preview")

    def get_image(url):
        r = requests.get(url)
        return BytesIO(r.content)


    if url:
        # preview = link_preview(url)
        # st.image(get_image(preview.image), caption=preview.site_name)
        # st.title(preview.title)
        # st.write("description:", preview.description)
        gen(url)
        
    else:
        st.write("Looks like you have'nt Entered a URL to preview")