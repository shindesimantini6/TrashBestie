import streamlit as st



import sys
import os

# Add the path to the parent folder of the current script's directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import settings

# Now you can import the settings module
# from settings import DETECT_LOCATOR, DETECTION_MODEL, SOURCES_LIST, DEFAULT_IMAGE, DEFAULT_DETECT_IMAGE, IMAGE


import PIL
import torch
import cv2
from pathlib import Path
import helper
from class_description import class_descriptions
import os

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Welcome to Garbage Image Detection! 👋")

st.markdown(
    """
## Detect Garbage Objects by Uploading Images 📷

In this section, you can easily upload images and have our advanced YOLOv8 model identify and classify garbage objects present in the image. Not only will you receive an accuracy score for each detected garbage type, but you'll also get guidance on how to correctly sort the garbage for proper disposal.

## ## How It Works

1. **Choose an Image**: Click on the "Upload Image" button to choose an image containing garbage objects.

2. **Object Detection**: Our YOLOv8 model will analyze the image and identify various garbage objects with corresponding accuracy scores.

3. **Garbage Sorting**: For each detected garbage object, you'll learn how to correctly sort it (e.g., recycling, compost, landfill).

Ready to start? Click on the "Upload Image" button and see the power of AI in action as it identifies garbage objects and helps you become a better waste warrior.

Remember, every step counts toward reducing waste and preserving our environment for future generations. Let's work together for a cleaner, greener planet!

**Click on "Upload Image" to get started with garbage object detection and sorting!**
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
    save_radio = st.sidebar.radio("Download image", ["Yes", "No"])
    save = True if save_radio == 'Yes' else False
    col1, col2 = st.columns(2)

    # with col1:
    #     if source_img is None:
    #         default_image_path = str(settings.DEFAULT_IMAGE)
    #         image = PIL.Image.open(default_image_path)
    #         st.image(default_image_path, caption='Default Image',
    #                  use_column_width=True)
    #     else:
    #         image = PIL.Image.open(source_img)
    #         st.image(source_img, caption='Uploaded Image',
    #                  use_column_width=True)

    if st.sidebar.button('Detect Objects'):
        with col1:
        # if source_img is None:
        #     default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
        #     image = PIL.Image.open(default_detected_image_path)
        #     st.image(default_detected_image_path, caption='Detected Image',
        #              use_column_width=True)
        # else:
            
            with torch.no_grad():
                classes_predicted = []
                image = PIL.Image.open(source_img)
                # st.image(source_img, caption='Uploaded Image',
                #         use_column_width=True)

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
        with col2:    
            for keys in class_descriptions:
                print(keys)
                for name in classes_predicted:
                    print(name)
                    if name == keys:
                        st.sidebar.write(f"Predicted as {name}")
                        st.write(class_descriptions[keys]["waste_bin"])
                        st.write(class_descriptions[keys]["description"])
