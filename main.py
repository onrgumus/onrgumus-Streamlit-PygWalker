import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

df = pd.read_csv("kaggle_income.csv", encoding='latin-1')

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="PygWalker in Streamlit",
    page_icon="🚶‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

class UsefulLinks:
    def __init__(self, links_dict):
        self.links_dict = links_dict
    
    def display_links(self):
        links_html = '<div style="display:flex; justify-content: space-between;">'
        for link_name, link_url in self.links_dict.items():
            links_html += f'<a href="{link_url}" target="_blank">{link_name}</a>'
        links_html += '</div>'
        st.markdown(links_html, unsafe_allow_html=True)

# Links
information = {
    "Data": "https://www.kaggle.com/datasets/goldenoakresearch/us-household-income-stats-geo-locations/code",
    "PyGWalker": "https://github.com/Kanaries/pygwalker",
    "PyGWalker with Streamlit": "https://docs.kanaries.net/pygwalker/use-pygwalker-with-streamlit"
}

# Add Title
page_title = "PygWalker in Streamlit"
st.write(f"<h1 style='text-align: center;'>{page_title}</h1>", unsafe_allow_html=True) 

# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
st.write("---")

st.header("PygWalker Features")
st.markdown("""
## Data Science Related Features:
- **Customizable Charts:** Enables easy creation of charts tailored to the needs of data scientists.
- **Interactive Visualization:** Allows visualizing data interactively and dynamically.
- **Data Analysis Tools:** Provides necessary tools for data analysis, enhancing the workflow for data scientists.
""")

# Displaying links using the UsefulLinks class.
my_links = UsefulLinks(information)
my_links.display_links()

st.write("")


st.markdown("<p style='text-align: center; color: #555555;'>Created with 🐻 by <b>Onur Gumus</b></p>", unsafe_allow_html=True)


