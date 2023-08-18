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
WEBCAM = 'Webcam'
IMAGE = 'Image'

SOURCES_LIST = [WEBCAM, IMAGE]

# images
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'recycling.png'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'office_4_detected.jpg'

# model
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'


# Detected/segmented image dirpath locator
DETECT_LOCATOR = 'detect'
SEGMENT_LOCATOR = 'segment'


# Webcam
WEBCAM_PATH = 0