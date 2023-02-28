import streamlit as st
from streamlit.logger import get_logger
import lucky_day as mainpage
from dotenv import load_dotenv

LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="LuckyDay App",
    )

load_dotenv()


if __name__ == "__main__":  
    mainpage.run()
