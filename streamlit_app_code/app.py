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


# # Sidebar
# st.title("Object Detection using YOLOv8")
# st.write("Herzlich Willkommen")

# if st.button("Webcam aktivieren"):
#     # Setzen Sie den Radio-Button auf "Webcam"
#     source_radio = "Webcam"
# else:
#     source_radio= None

# st.sidebar.header("ML Model Config")

# nav = st.sidebar.radio(
#     "Please chose one of the following options:",
#     ["Home", "Webcam-Detection", "Image-Detection"]
#     ) 

# if nav == "Home":
#     st.markdown(
#     """ ## Welcome to the Garbage Predictor page.
#     """
#     )
#     st.image("https://www.bing.com/images/search?view=detailV2&ccid=RvwE8IJ5&id=E6038CEEC59C8C4510724BCA3AA881115B1B1A60&thid=OIP.RvwE8IJ5ZmpW4taP_LjxwQHaGA&mediaurl=https%3a%2f%2fi1.wp.com%2fallamerican1930.com%2fwp-content%2fuploads%2f2020%2f10%2f12oz-can-cluster.png%3ffit%3d1766%2c1434%26ssl%3d1&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.46fc04f08279666a56e2d68ffcb8f1c1%3frik%3dYBobWxGBqDrKSw%26pid%3dImgRaw%26r%3d0&exph=1434&expw=1766&q=alumium+cans&simid=608009744375158927&FORM=IRPRST&ck=445AC1BD63720DC4B47B403E6A96DF41&selectedIndex=0&ajaxhist=0&ajaxserp=0", width=400)
    
#     st.markdown(
#     """ ### This model predicts the garbage type based on YOLOv8 object detection. Furthermore it gives you the information of how to sort it correctly.
#     """
#     )

# if nav == "Webcam-Detection":
#     st.write("Welcome to the section of Webcam-Detection. Please hold your garbage sort into the webcam of your electronic device")
#     st.write("Data is taken from [titanic](https://www.kaggle.com/competitions/titanic/data?select=train.csv)")
#     if st.checkbox("Click here to see the original dataframe"):
#         st.title("Titanic training dataset")
#         st.dataframe(df)
#     if st.checkbox("Click here to see missing values"):
#         fig,ax = plt.subplots()
#         st.title("Heatmap features titanic dataset")
#         sns.heatmap(df.corr(), ax = ax)
#         st.write(fig)
#     if st.checkbox("Click here to see distribution of variables"):
#         st.title("Distribution features titanic dataset")
#         fig = sns.pairplot(df, hue = "Survived")
#         st.pyplot(fig)
#     if st.checkbox("Click here to see the variables taken into account for model fit"):
#         st.title("Features for model fit")
#         st.write(df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].columns)

# if nav == "Image-Detection":
#     st.markdown(
#     """ #### Welcome to the predictions page.
#     """
#     )

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

elif source_radio == settings.WEBCAM:
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