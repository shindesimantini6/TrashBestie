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
# WEBCAM = 'Webcam'

# SOURCES_LIST = [WEBCAM]

# model
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'


# Detected/segmented image dirpath locator
DETECT_LOCATOR = 'detect'
SEGMENT_LOCATOR = 'segment'


# Webcam
WEBCAM_PATH = 0