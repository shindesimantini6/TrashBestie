from pathlib import Path
import sys
import cv2

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Source
IMAGE = 'Image'
WEBCAM = 'Webcam'

SOURCES_LIST = [WEBCAM, IMAGE]

# images
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'office_4.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'office_4_detected.jpg'

# VIDEOS_DICT = {
#     'video_1': VIDEO_1_PATH,
#     'video_2': VIDEO_2_PATH,
#     'video_3': VIDEO_3_PATH,
#     'video_4': VIDEO_4_PATH,
# }

# model
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'


# Detected/segmented image dirpath locator
DETECT_LOCATOR = 'detect'
SEGMENT_LOCATOR = 'segment'


# Webcam
WEBCAM_PATH = 0


# def process_video(input_video_path, output_video_path):
#     cap = cv2.VideoCapture(str(input_video_path))

#     # Get the video frame rate
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     # Define the codec for the output video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#     # Get the size of the video frame
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create the VideoWriter object
#     out = cv2.VideoWriter(str(output_video_path), fourcc, fps, (width, height))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Process the frame here
#         processed_frame = frame  # Replace this line with your own code to process the frame

#         # Write the processed frame to the output video
#         out.write(processed_frame)

#     cap.release()
#     out.release()

# # Process the video and save the output to a file
# input_video_path = VIDEOS_DICT['video_1']
# output_video_path = VIDEO_DIR / 'king_bolete_processed.mp4'
# process_video(input_video_path, output_video_path)