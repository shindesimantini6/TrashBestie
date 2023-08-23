import streamlit as st
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
    page_title="ImageDetection",
    page_icon="🗑️",
)

# Add a confidence level limit
conf = 0.4  # Minimum accuracy score fixed at 50%

# Paths to the trained model
dirpath_locator = settings.DETECT_LOCATOR
model_path = Path(settings.DETECTION_MODEL)

# Load the model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")


# Uploaded image
source_img = None
source_img = st.sidebar.file_uploader("Choose an image", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
save = True  # Save images

# Create columns
col1, col2 = st.columns(2)

# Predict objects in the image
if source_img:
    with col1:        
        with torch.no_grad():
            classes_predicted = []
            image = PIL.Image.open(source_img)
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
        # Write the predicted values and descriptions  
        for keys in class_descriptions:
            print(keys)
            for name in classes_predicted:
                print(name)
                if name == keys:
                    st.write(f"### Predicted as {name}")
                    st.write(f'### {class_descriptions[keys]["waste_bin"]}')
                    st.write(class_descriptions[keys]["description"])
