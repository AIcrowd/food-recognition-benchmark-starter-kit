import random
import json
import numpy as np
import argparse
import base64
import glob
import os
from PIL import Image

results = []

padding = 50
SEGMENTATION_LENGTH = 10
MAX_NUMBER_OF_ANNOTATIONS = 10

VALID_CATEGORIES =  [1565, 1010, 1085, 2053, 1310, 2578, 1154, 2620, 1566, 1151, 2939, 1040, 1070, 2580, 2512, 1056, 1069, 2131, 2521, 2022, 1026, 1068, 1022, 2750, 1468, 1013, 1078, 2738, 1061, 2618, 1311, 1163, 2504, 2498, 1788, 2099, 1032, 1505, 1058, 1554]


IMAGES_DIR = os.getenv("AICROWD_TEST_IMAGES_DIR", "data/val/images")

def get_image_id_from_image_path(image_path):
    """
    image_path : /home/testsdir/098767.jpg 
    image_id : 98767
    """
    filename = os.path.basename(image_path)
    filename = filename.replace(".jpg", "")
    image_id = int(filename)
    return image_id

print("Generating random results file....")

for _idx, image_path in enumerate(glob.glob(os.path.join(IMAGES_DIR, "*.jpg"))):

    image_id = get_image_id_from_image_path(image_path)

    im = Image.open(image_path)
    img_width, img_height = im.size

    _result = {}
    _result["image_id"] = image_id
    _result["category_id"] = random.choice(VALID_CATEGORIES) 
    _result["score"] = np.random.rand()
    x = random.randint(0, img_width-padding)
    y = random.randint(0, img_height-padding)
    width = random.randint(0, img_width-x)
    height = random.randint(0, img_height-y)
    _result["bbox"] = [x, y, img_width, img_height]

    _segmentation=[]
    for k in range(SEGMENTATION_LENGTH*2):
        _segmentation.append(np.random.randint(0, img_width))
        _segmentation.append(np.random.randint(0, img_height))
    _result["segmentation"] = [_segmentation]

    results.append(_result)

print("Writing results to : data/result_annotations.json")
ANNOTATIONS_OUTPUT_PATH = os.getenv("ANNOTATIONS_OUTPUT_PATH", "./result_annotations.json")
with open(ANNOTATIONS_OUTPUT_PATH, "w") as fp:
    fp.write(json.dumps(results))
print("Writing Complete !")

