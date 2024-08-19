import streamlit as st

# Define the MultiPage class to manage multiple Streamlit pages
class MultiPage:

    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio(
            'Menu',
            self.pages,
            format_func=lambda page: page['title']
        )

        # Run the selected page function
        page['function']()
