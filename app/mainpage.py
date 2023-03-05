
import streamlit as st
from PIL import Image
import pathlib 
import os

def run():
    st.markdown("# Lucky Day")
    st.markdown("**Conduct your transactions via a transparent, trustworthy decentralized network**")

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    image_path = os.path.join(parent_path, "app/Images/mainpage.jpeg")
  
    mainpage_image = Image.open(image_path)
    new_image = mainpage_image.resize((600, 400))
    st.image(new_image)
    
