from pathlib import Path
import PIL

import streamlit as st
import torch
import cv2
import pafy

import settings
import helper

import os
os.environ["PAFY_BACKEND"] = "internal"
import pafy

# Sidebar
st.title("Object Detection using YOLOv8")

# Set the default values
mlmodel_radio = 'Detection'
conf = 0.5  # Minimum accuracy score fixed at 50%

# Load model based on the selected task
if mlmodel_radio == 'Detection':
    dirpath_locator = settings.DETECT_LOCATOR
    model_path = Path(settings.DETECTION_MODEL)
elif mlmodel_radio == 'Segmentation':
    dirpath_locator = settings.SEGMENT_LOCATOR
    model_path = Path(settings.SEGMENTATION_MODEL)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")

source_img = None
st.sidebar.header("Source")
source_radio = st.sidebar.radio(
    "Select the source you want to detect", settings.SOURCES_LIST)

# body

if source_radio == settings.WEBCAM:
    source_webcam = settings.WEBCAM_PATH
    #if st.sidebar.button('Detect Objects'):
    vid_cap = cv2.VideoCapture(source_webcam)
    stframe = st.empty()
    while (vid_cap.isOpened()):
        success, image = vid_cap.read()
        if success:
            image = cv2.resize(image, (720, int(720*(9/16))))
            res = model.predict(image, conf=conf)
            res_plotted = res[0].plot()
            stframe.image(res_plotted,
                            caption='Detected Video',
                            channels="BGR",
                            use_column_width=True
                            )