import streamlit as st
from streamlit.logger import get_logger
import lucky_day as mainpage

LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="LuckyDay App",
    )
    

if __name__ == "__main__":  
    mainpage.run()
