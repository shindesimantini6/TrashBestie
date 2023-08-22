import streamlit as st

option = st.sidebar.selectbox(
    'What would you like to know about?',
    ('Webcam Detection', 'Image Upload Detection'))

if option == 'Webcam Detection':
    st.header("Webcam Detection")

    st.write(
        """
    You can use your webcam to detect and identify various garbage objects in real time. 
    Simply hold the object in front of your webcam, and our advanced object detection algorithm will identify the garbage objects on the screen.

    ### How It Works

    1. **Select Webcam Detection**

    2. **Show Objects to Your Webcam** :  
    Hold any object in front of your webcam. The app will automatically detect and label the garbage objects present.

    3. **Real-Time Results** :  
    Watch as the app identifies the type of garbage object and provides information about its proper disposal.
    """
    )

else:
    st.header("Image Upload Detection")

    st.write(
        """
    You can easily upload images and have our advanced object detection algorithm identify and classify garbage objects present in the image. 
    Not only will you receive an accuracy score for each detected garbage type, 
    but you'll also get guidance on how to correctly sort the garbage for proper disposal.

    ## How It Works

    1. **Upload an Image** :   
        Click on the "Upload Image" button to choose an image containing garbage objects. Image size limited to 200MB per file and types allowed are JPG, JPEG, PNG, BMP and WEBP.

    2. **Object Detection** :   
        Our YOLOv8 model will analyze the image and identify various garbage objects with corresponding accuracy scores.

    3. **Garbage Sorting** :   
        For each detected garbage object, you'll learn how to correctly sort it (e.g., recycling, compost, landfill).

    """
    )
