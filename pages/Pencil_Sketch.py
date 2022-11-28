import streamlit as st
import numpy as np
from PIL import Image
import cv2
import json
from streamlit_lottie import st_lottie
st.title("✏Pencil Sketch")
st.subheader("This feature will allow you to convert your image into a Pencil Sketch")
st.subheader("“A line is a dot that went for a walk.” - Paul Klee")
st.text("Sketching allows us to get our ideas down quickly without overthinking them, or even dismissing them before they've even left our brains.\n It allows us explore ideas and to clear our minds, brainstorm, plan things out quickly and think away from the restrictions of the \ncomputer screen.")
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def dodgeV2(x,y):
    return cv2.divide(x,255-y,scale=256)

def pencil_sketch(img):
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_inv=cv2.bitwise_not(img_gray)
    img_smoothning=cv2.GaussianBlur(img_inv,(21,21),sigmaX=0,sigmaY=0)
    final_img=dodgeV2(img_gray,img_smoothning)
    return final_img
def main_loop():
    load_lottie=load_lottiefile("C:\\Users\\Restart\\Downloads\\91979-border-path.json")
    st_lottie(
        load_lottie,
        reverse=False,
        loop=True,
        quality="high",
        width=1200,
        height=500,
        key=None,
    )
    image_file=st.file_uploader("Upload your image",["jpg","jpeg","png"])
    if not image_file:
        return None
   
    original_image=Image.open(image_file)
    original_image=np.array(original_image)
    processed_image=pencil_sketch(original_image)
    st.text("Original Image VS Processed Image")
    st.write("Input image")
    st.image(original_image,use_column_width=True)
    st.image(processed_image,use_column_width=True)
    load_lottie1=load_lottiefile("C:\\Users\\Restart\\Downloads\\16583-border.json")
    st_lottie(
        load_lottie1,
        reverse=False,
        loop=True,
        quality="high",
        width=1600,
        height=1600,
        key=None,
    )
    
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    main_loop()