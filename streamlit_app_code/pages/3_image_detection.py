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
                        image, save=save, save_txt=save, exist_ok=True, conf=conf)
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
