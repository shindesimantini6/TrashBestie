import streamlit as st
import settings
import PIL
import torch
import cv2
from pathlib import Path
import helper
from class_description import class_descriptions
import os

st.set_page_config(
    page_title="WebcamDetection",
    page_icon="🗑️",
)

conf = 0.2  # Minimum accuracy score fixed at 50%

dirpath_locator = settings.DETECT_LOCATOR
model_path = Path(settings.DETECTION_MODEL)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")

source_img = None
# source_radio = st.sidebar.radio("Select source", settings.SOURCES_LIST)
source_webcam = settings.WEBCAM_PATH

vid_cap = cv2.VideoCapture(source_webcam)
stframe = st.empty()
while (vid_cap.isOpened()):
    success, image = vid_cap.read()
    if success:
        classes_predicted = []
        image = cv2.resize(image, (720, int(720*(9/16))))
        res = model.predict(image, conf=conf)
        names = model.names
        for r in res:
            for c in r.boxes.cls:
                classes_predicted.append(names[int(c)])
        print(classes_predicted)


        res_plotted = res[0].plot() 
        stframe.image(res_plotted,
                        caption='Detected Video',
                        channels="BGR",
                        use_column_width=True
                        )
        for keys in class_descriptions:
            print(keys)
            for name in classes_predicted:
                print(name)
                if name == keys:
                    st.write(f"Predicted as {name}")
                    st.write(class_descriptions[keys]["waste_bin"])
                    st.write(class_descriptions[keys]["description"])
