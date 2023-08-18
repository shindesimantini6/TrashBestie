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
st.title("Garbige Detection & assorting help using YOLOv8")

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

# Add a description to the "Information" header
st.sidebar.header("Information")
st.sidebar.write("This section provides additional information about the application.")

# Categories with indentation using Markdown
st.sidebar.write("Aluminium can: This garbage has to be sorted XXX",
                 "\n\n",
                 "Battery: XXX"
                 "\n\n",
                 "Pen: XXX",
                 "\n\n",
                 "Leftovers: XXX",
                 "\n\n",
                 "Toothbrushes: XXX",
                 "\n\n")
                 
# st.sidebar.write("Aluminium can: This garbage has to be sorted XXX", 
#                  "Battery: XXX",
#                  "Pen: XXX",
#                  "Leftovers: XXX",
#                  "Toothbrushes: XXX")
# source_radio = st.sidebar.radio(
#     "Information", settings.SOURCES_LIST)

# body


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
        
st.markdown(
    """
    <style>
    .stApp {
        background-color: #252525
    }

    """
)