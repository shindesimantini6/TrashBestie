
<img width="629" alt="trashbestie_black" src="https://github.com/shindesimantini6/TrashBestie/assets/79316344/5c3a2352-ba64-4959-a3fd-17b7c9373d7e">

An app used to sort waste at home.

Sorting waste, also at home, can be tricky. For example a toothbrush which is suppose to be thrown away in the black bin is easily confused and thrown into the yellow bin or the pizza boxes with oil all over the box is thrown into blue but belongs in the black bin. Such mistakes, mean the garbage is incinerated at the garbage sorting stations, as sorting waste is time-consuming and expensive. Hence it is very important to sort garbage correctly at home. 

The version 1 of TrashBestie is a custom [Yolov8](https://github.com/ultralytics/ultralytics) model trained to detect `aluminium cans`, `pens`, `toothbrushes` and `batteries` and deployed on to a [Streamlit](https://streamlit.io/) Web app. The user can scan the images or upload the images into the app. All predictions are with a minimum level 50% confidence.

The waste sorting currently is based on the waste segregation system in Germany.

## Method
1. We identified most confusing waste categories, and picked 4 most common for our version 1.
2. We obtained the data in two ways:  
    a. [Open Data Source](https://github.com/AgaMiko/waste-datasets-review)  
    b. Took images ourselves with the garbage from home. This step was taken to improve the accuracy of our model as garbage looks different in different countries and the [open source](https://github.com/AgaMiko/waste-datasets-review) has garbage not necessarily from Germany.  
3. We annotated, preprocessed and augmented all images in [Roboflow](https://roboflow.com/).
4. Trained a [YOLOv8](https://github.com/ultralytics/ultralytics) model for all images with 4 classes (`aluminium-cans`, `pen`, `toothbrushes` and `battery`). More information on training a custom YOLOv8 model with data augmented and preprocessed in Roboflow [here](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/).
5. Created a [Streamlit web app](https://streamlit.io/) with the Webcam and Image Detection feature. More information on with YOLOv8 streamlit detection [here](https://github.com/CodingMantras/yolov8-streamlit-detection-tracking).

## Usage

- Run `streamlit run Home.py` to open the web app.
- The app should open in a new browser window.

## Webcam Detection
1. Change the source of your webcam in `settings.py` at   
```
# Webcam
WEBCAM_PATH = {path to webcam}
```
2. The predicted class will be displayed, as the model detects the objects, along with where the garbage is to be disposed and an explanation for why the garbage is to 
be diposed in that bin. 

## Image Detection
1. Upload an image by clicking on the "Browse files" button.
2. The uploaded image with the detected objects will be displayed on the page, along with the predicted garbage class, where the garbage is to be disposed and an explanation for why the garbage is to 
be diposed in that bin. 
3. Click the "Download Image" button to download the image.

## Demo of the model

![Screenshot from 2023-08-23 12-03-35_cropped](https://github.com/shindesimantini6/TrashBestie/assets/79316344/d7e6a1ce-9160-4f4b-9f63-d6e1e5d1a3ed)

## Demo of the Web App

https://github.com/shindesimantini6/TrashBestie/assets/79316344/607ad584-9523-410d-b64a-6174e4e29640

## Requirements
- Python 3.6+
- YOLOv8
- Streamlit 
- OpenCV
- Tensorflow

## Collaborators
- [My](https://www.linkedin.com/in/my-huynh/) 
- [Helge](https://github.com/helge1991)
- [Simantini](https://github.com/shindesimantini6)
