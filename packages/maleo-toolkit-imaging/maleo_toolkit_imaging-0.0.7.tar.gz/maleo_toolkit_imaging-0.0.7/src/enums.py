from enum import StrEnum


class ColorSpace(StrEnum):
    RGB = "rgb"
    GRAYSCALE = "grayscale"


class ImageFormat(StrEnum):
    PNG = "png"


class OutputType(StrEnum):
    BASE_64 = "base64"
    RAW = "raw"
    FILE = "file"


# Class names (COCO / X-ray / dsb)
CLASS_NAMES = [
    "Atelectasis",
    "Calcification",
    "Cardiomegaly",
    "Consolidation",
    "Infiltration",
    "Lung Opacity",
    "Lung cavity",
    "Nodule/Mass",
    "Pleural Effusion",
    "Pneumothorax",
    "Tuberculosis",
]

# Image processing defaults
IMAGE_SIZE = 512
NORM_MEAN = [0.485, 0.456, 0.406]
NORM_STD = [0.229, 0.224, 0.225]

# Loss params
GLOBAL_FOCAL_GAMMA = 1.5
GLOBAL_FOCAL_ALPHA = 0.5
