import streamlit as st
# from streamlit_app_code import settings

import sys
import os

# Add the path to the parent folder of the current script's directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import settings

import PIL
import torch
import cv2
from pathlib import Path
import helper
from class_description import class_descriptions
import os

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Real-Time Garbage Object Detection! 👋")

st.markdown(
    """
## Detect Garbage Objects with Your Webcam 📷

With this section, you can use your webcam to detect and identify various garbage objects in real time. Simply show the object in front of your webcam, and our advanced object detection algorithm will identify and highlight the garbage objects on the screen.

## How It Works

1. **Select Webcam Detection**: Choose the "Webcam Detection" option from the sidebar to get started.

2. **Show Objects to Your Webcam**: Hold any object in front of your webcam. The app will automatically detect and label the garbage objects present.

3. **Real-Time Results**: Watch as the app identifies the type of garbage object and provides information about its proper disposal.

## Join Us in Keeping the Environment Clean

Whether you're passionate about recycling, waste reduction, or simply curious about what's considered garbage, our Real-Time Garbage Object Detection app is a fun and educational way to contribute to a cleaner world.

Ready to get started? Choose the "Webcam Detection" option from the sidebar and let's begin the garbage object detection journey together!

Remember, every small action counts toward a cleaner and greener planet. Let's make a positive impact!

**Select "Webcam Detection" from the sidebar to start detecting garbage objects in real time!**
"""
)

conf = 0.5  # Minimum accuracy score fixed at 50%

dirpath_locator = settings.DETECT_LOCATOR
model_path = Path(settings.DETECTION_MODEL)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")

source_img = None
source_radio = st.sidebar.radio("Select source", settings.SOURCES_LIST)

if source_radio == settings.WEBCAM:
    source_webcam = settings.WEBCAM_PATH
#    if st.sidebar.button('Detect Objects'):
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
                        st.sidebar.write(f"Predicted as {name}")
                        st.write(class_descriptions[keys]["waste_bin"])
                        st.write(class_descriptions[keys]["description"])
