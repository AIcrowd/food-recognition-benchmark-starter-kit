import random
import json
import numpy as np
import argparse
import base64
import glob
import os
import traceback
from PIL import Image
import aicrowd_helpers


"""
Expected ENVIRONMENT Variables

* AICROWD_TEST_IMAGES_PATH : abs path to  folder containing all the test images
* AICROWD_PREDICTIONS_OUTPUT_PATH : path where you are supposed to write the output predictions.json
"""

# Configuration Variables
padding = 50
SEGMENTATION_LENGTH = 10
MAX_NUMBER_OF_ANNOTATIONS = 10
# List of valid categories to choose from
VALID_CATEGORIES =  [1565, 1010, 1085, 2053, 1310, 2578, 1154, 2620, 1566, 1151, 2939, \
    1040, 1070, 2580, 2512, 1056, 1069, 2131, 2521, 2022, 1026, 1068, 1022, 2750, 1468, \
    1013, 1078, 2738, 1061, 2618, 1311, 1163, 2504, 2498, 1788, 2099, 1032, 1505, 1058, \
    1554]


# Helper functions
def bounding_box_from_points(points):
    """
        This function only supports the `poly` format.
    """
    points = np.array(points).flatten()
    even_locations = np.arange(points.shape[0]/2) * 2
    odd_locations = even_locations + 1
    X = np.take(points, even_locations.tolist())
    Y = np.take(points, odd_locations.tolist())
    bbox = [X.min(), Y.min(), X.max()-X.min(), Y.max()-Y.min()]
    bbox = [int(b) for b in bbox]
    return bbox

def single_segmentation(image_width, image_height, number_of_points=10):
    points = []
    for k in range(number_of_points):
        # Choose a random x-coordinate
        random_x = int(random.randint(0, image_width))
        # Choose a random y-coordinate
        random_y = int(random.randint(0, image_height))
        #Flatly append them to the list of points
        points.append(random_x)
        points.append(random_y)
    return [points]

def single_annotation(image_id, number_of_points=10):
    width, height = get_image_width_height(image_id)
    _result = {}
    _result["image_id"] = image_id
    """
    Valid Categories are embedded in the annotations.json of the training set
    """
    _result["category_id"] = random.choice(VALID_CATEGORIES) 
    
    _result["score"] = np.random.rand() # a random score between 0 and 1

    _result["segmentation"] = single_segmentation(width, height, number_of_points=number_of_points)
    _result["bbox"] = bounding_box_from_points(_result["segmentation"])
    return _result


def get_image_id_from_image_path(image_path):
    """
    Returns the image_id from the image_path of a file in the test set
    image_path : /home/testsdir/098767.jpg 
    image_id : 98767
    """
    filename = os.path.basename(image_path)
    filename = filename.replace(".jpg", "")
    image_id = int(filename)
    return image_id

def gather_images(test_images_path):
    images = glob.glob(os.path.join(
        test_images_path, "*.jpg"
    ))
    return images

def gather_image_ids(test_images_path):
    images = gather_images(test_images_path)
    filenames = [os.path.basename(image_path).replace(".jpg","") for image_path in images]
    image_ids = [int(x) for x in filenames]
    return image_ids

def get_image_path(image_id):
    test_images_path = os.getenv("AICROWD_TEST_IMAGES_PATH", False)
    return "{}.jpg".format(os.path.join(test_images_path, str(image_id).zfill(6)))

def get_image_width_height(image_id):
    image_path = get_image_path(image_id)
    im = Image.open(image_path)
    width, height = im.size
    im.close()
    return width, height

def gather_input_output_path():
    test_images_path = os.getenv("AICROWD_TEST_IMAGES_PATH", False)
    assert test_images_path != False, "Please provide the path to the test images using the environment variable : AICROWD_TEST_IMAGES_PATH"

    predictions_output_path = os.getenv("AICROWD_PREDICTIONS_OUTPUT_PATH", False)
    assert predictions_output_path != False, "Please provide the output path (for writing the predictions.json) using the environment variable : AICROWD_PREDICTIONS_OUTPUT_PATH"

    return test_images_path, predictions_output_path


def run():
    ########################################################################
    # Register Prediction Start
    ########################################################################
    aicrowd_helpers.execution_start()

    ########################################################################
    # Gather Input and Output paths from environment variables
    ########################################################################
    test_images_path, predictions_output_path = gather_input_output_path()

    ########################################################################
    # Gather Image IDS
    ########################################################################
    image_ids = gather_image_ids(test_images_path)

    ########################################################################
    # Generate Predictions
    ########################################################################
    predictions = []
    for image_id in image_ids:
        number_of_annotations = random.randint(0, MAX_NUMBER_OF_ANNOTATIONS)
        for _idx in range(number_of_annotations):
            _annotation = single_annotation(image_id)
            predictions.append(_annotation)
        ########################################################################
        # Register Prediction
        #
        # Note, this prediction register is not a requirement. It is used to
        # provide you feedback of how far are you in the overall evaluation.
        # In the absence of it, the evaluation will still work, but you
        # will see progress of the evaluation as 0 until it is complete
        #
        # Here you simply announce that you completed processing a set of
        # image-ids
        ########################################################################
        aicrowd_helpers.execution_progress({
            "image_ids" : [image_id]
        })


    # Write output
    fp = open(predictions_output_path, "w")
    fp.write(json.dumps(predictions))
    fp.close()
    ########################################################################
    # Register Prediction Complete
    ########################################################################
    aicrowd_helpers.execution_success({
        "predictions_output_path" : predictions_output_path
    })

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        error = traceback.format_exc()
        print(error)
        aicrowd_helpers.execution_error(error)
