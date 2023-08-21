from pathlib import Path
import PIL

import streamlit as st
import torch
import cv2
# import pafy

import settings
import helper
from class_description import class_descriptions

import os
# os.environ["PAFY_BACKEND"] = "internal"
# import pafy


# Sidebar
# st.title("Object Detection using YOLOv8")

# st.sidebar.header("ML Model Config")

dirpath_locator = settings.DETECT_LOCATOR
model_path = Path(settings.DETECTION_MODEL)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")

source_img = None
source_radio = st.sidebar.radio("Select source", settings.SOURCES_LIST)

# bodyma
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader("Choose an image", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    save_radio = st.sidebar.button("Download image", ["Yes", "No"])
    save = True if save_radio == 'Yes' else False
    col1, col2 = st.columns(2)

    with col1:
        if source_img is None:
            default_image_path = str(settings.DEFAULT_IMAGE)
            image = PIL.Image.open(default_image_path)
            st.image(default_image_path, caption='Default Image',
                     use_column_width=True)
        else:
            image = PIL.Image.open(source_img)
            st.image(source_img, caption='Uploaded Image',
                     use_column_width=True)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            image = PIL.Image.open(default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                with torch.no_grad():
                    classes_predicted = []
                    res = model.predict(
                        image, save=save, save_txt=save, exist_ok=True)
                    names = model.names
                    for r in res:
                        for c in r.boxes.cls:
                            classes_predicted.append(names[int(c)])
                    print(classes_predicted)

                    boxes = res[0].boxes
                    res_plotted = res[0].plot()[:, :, ::-1]
                    # print(res_plotted)
                    st.image(res_plotted, caption='Detected Image',
                             use_column_width=True)
                    IMAGE_DOWNLOAD_PATH = f"runs/{dirpath_locator}/predict/image0.jpg"
                    with open(IMAGE_DOWNLOAD_PATH, 'rb') as fl:
                        st.download_button("Download object-detected image",
                                           data=fl,
                                           file_name="image0.jpg",
                                           mime='image/jpg'
                                           )
                
                for keys in class_descriptions:
                    print(keys)
                    for name in classes_predicted:
                        print(name)
                        if name == keys:
                            st.sidebar.write(f"Predicted as {name}")
                            st.write(class_descriptions[keys]["waste_bin"])
                            st.write(class_descriptions[keys]["description"])

elif source_radio == settings.VIDEO:
    source_vid = st.sidebar.selectbox(
        "Choose a video...", settings.VIDEOS_DICT.keys())
    video_file = open(settings.VIDEOS_DICT.get(source_vid), 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    if st.sidebar.button('Detect Video Objects'):
        vid_cap = cv2.VideoCapture(str(settings.VIDEOS_DICT.get(source_vid)))
        stframe = st.empty()
        while (vid_cap.isOpened()):
            success, image = vid_cap.read()
            if success:
                image = cv2.resize(image, (720, int(720*(9/16))))
                res = model.predict(image)
                res_plotted = res[0].plot()
                stframe.image(res_plotted,
                              caption='Detected Video',
                              channels="BGR",
                              use_column_width=True
                              )

elif source_radio == settings.WEBCAM:
    source_webcam = settings.WEBCAM_PATH
#    if st.sidebar.button('Detect Objects'):
    vid_cap = cv2.VideoCapture(source_webcam)
    stframe = st.empty()
    while (vid_cap.isOpened()):
        success, image = vid_cap.read()
        if success:
            image = cv2.resize(image, (720, int(720*(9/16))))
            res = model.predict(image)
            # if res == "battery":
            #     description = ""
            #     print(description)
            # if res =


            res_plotted = res[0].plot() 
            stframe.image(res_plotted,
                            caption='Detected Video',
                            channels="BGR",
                            use_column_width=True
                            )

#st.markdown(
#    """
#    <style>
#    .css-6qob1r{
#       background-color: #262730
#    }
#    .css-1wrcr25,
#    .css-18ni7ap{
#       background-color: black;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)