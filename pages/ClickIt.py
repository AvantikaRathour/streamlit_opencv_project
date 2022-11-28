import streamlit as st
import cv2
import datetime
import json
from streamlit_lottie import st_lottie
st.title("ClickIt.....")
st.subheader("This is just an opened webcam with time and date snap ")
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def video_capture():
    cap=cv2.VideoCapture(0);
         
    
    frame_window=st.image([])
    while(cap.isOpened()):
        ret,frame=cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        font=cv2.FONT_HERSHEY_PLAIN
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,30),font,1,(0,0,0),2,cv2.LINE_AA)
        frame_window.image(frame)
        if cv2.waitKey(1) == ord("e"):
           break
    cap.release()
    cv2.destroyAllWIndows()
    

def main_loop():
    load_lottie1=load_lottiefile("C:\\Users\\Restart\Downloads\\68898-cameras-and-photography.json")
    st_lottie(
        load_lottie1,
        reverse=False,
        loop=True,
        quality="high",
        width=600,
        height=600,
        key=None,
    )
    st.text("Processed Video")
    # frame_window=st.image([])
    run=st.checkbox("Run")
    while run:
      video_capture()
    # st.image([frame])
    
    

# import cv2
# import streamlit as st


# def main_loop():
#    st.title("Webcam Live Feed")
#    run = st.checkbox('Run')
#    FRAME_WINDOW = st.image([])
#    camera = cv2.VideoCapture(0)

#    while run:
#       _, frame = camera.read()
#       FRAME_WINDOW.image(frame)
#    else:
#       st.write('Stopped')
    
if __name__=="__main__":
    main_loop()
      