import streamlit as st

from streamlit_option_menu import option_menu

import Home ,Account ,Test,My_DataBase;



# st.set_page_config(page_title ="Link Preview Gen", page_icon = "🔗", initial_sidebar_state = "auto")

class MultiApp:
    
    def __init__(self):
        self.apps=[]
        
    def add_app(self, title, func):
        self.apps.append({
			"title": title,
			"function": func
		}) 
        
    def run():
        
        with st.sidebar:
            app = option_menu(
				menu_title='Link_Preview_Gen',
				options=['Home','Account','My_DataBase','Test'],
				icons=['🏠','👤','🧪','🗃️'],
				menu_icon='🔗',
				default_index=0,
				styles={
                    "container": {"padding": "5!important","background-color":'black'},
        			"icon": {"color": "white", "font-size": "23px"}, 
        			"nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        			"nav-link-selected": {"background-color": "#02ab21"},}
    
			)
            
        if app=='Home':
            Home.app()
        if app=='Account':
            Account.app()
        if app=='Test':
            Test.app() 
        if app=='My_DataBase':
            My_DataBase.app()       
            
        
        
    run()               

                