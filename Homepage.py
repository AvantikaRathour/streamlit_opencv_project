import streamlit as st 
import json
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Image Processing",page_icon="✨",layout="wide")
st.title("Image Processing✨")
st.subheader("Welcome , we are providing an interactive platform to process your images and try some other features        of computer vision")
st.sidebar.title("Select a page")
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def main_loop():
    lottie_coding=load_lottiefile("C:\\Users\\Restart\\Downloads\\61067-website-design.json")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=500,
        width=800,
        key=None,
    )
if __name__=="__main__":
    main_loop()
   







































