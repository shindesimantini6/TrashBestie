import streamlit as st
from /streamlit_app_code import settings
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

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
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
