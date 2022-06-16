import streamlit as st
import cv2 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            <html><body><p></p><body/></html>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
detector = FaceDetector()
video = cv2.VideoCapture(0)
run = st.checkbox("Run/Stop")
frame = st.image([])
while run:
	success,capture = video.read()
	
	img,bboxs = detector.findFaces(capture)
	capture = cv2.cvtColor(capture,cv2.COLOR_BGR2RGB)

	Blur = cv2.GaussianBlur(capture,(5,5),2)
	
	#frame.image(capture)
	frame.image(Blur)


video.release()



