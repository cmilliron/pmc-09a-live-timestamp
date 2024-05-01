import cv2
import streamlit as st
from datetime import datetime
from time import sleep

st.title("Motion Detector")
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    check, frame = camera.read()
    sleep(1)
    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.putText(img=frame,
                    text=datetime.now().isoformat(),
                    org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

