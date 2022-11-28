import streamlit as st 
import cv2 
from PIL import Image
import numpy as np
import json
from streamlit_lottie import st_lottie
st.title("➡Play With Filter Effects")
st.subheader("You can analyse your browsed image in variety of effects ")
st.text("""This function will allow you to convert your image to grayish texture.\nYou can also apply shrpening effect and hdr effect to your image""")
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
       return json.load(f) 
def gray_image(image,amount):
    grayish=cv2.cvtColor(image,amount)
    return grayish
def inversion(img):
    ivn=cv2.bitwise_not(img)
    return ivn

def sharpening_effect(img):
    kernel=np.array([[-1,-1,-1],[-1,9.5,-1],[-1,-1,-1]])
    s_img=cv2.filter2D(img,-1,kernel)
    return s_img
def hdr(img):
    hdr_=cv2.detailEnhance(img,sigma_s=150,sigma_r=0.15)
    return hdr_
def main_loop():
    load_coding=load_lottiefile("C:\\Users\\Restart\\Downloads\\52599-ornament-animation.json")
    st_lottie(
        load_coding,
        reverse=False,
        speed=1,
        loop=True,
        quality="high",
        width=1300,
        height=200,
        key=None,
    )
    image_file=st.file_uploader("Upload your image",["jpg","png","jpeg"])
    if not image_file:
        return None
    original_image=Image.open(image_file)
    original_image=np.array(original_image)
    original_image1=Image.open(image_file)
    original_image=np.array(original_image1)
    

    processed_image=gray_image(original_image,cv2.COLOR_BGR2GRAY)
    processed_imag=sharpening_effect(original_image)
    processed_ima=hdr(original_image)
    st.text("Original_image VS Processed_image")
    st.image([original_image])
    st.text("Gray Filter")
    st.image([processed_image])
    st.text("Sharpened Image")
    st.image([processed_imag])
    st.text("HDR Effect")
    st.image([processed_ima])
    processed_image1=inversion(original_image)
    st.text("inversion in image")
    st.image([processed_image1])


if __name__=="__main__":
    main_loop()














