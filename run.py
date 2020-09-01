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
VALID_CATEGORIES =  [2578, 1157, 2022, 1198, 2053, 1566, 2099, 1554, 1151, 2530, 2521, 2534, 1026, 1311, 2738, 1505, 1078, 1116, 1731, 1453, 1040, 1538, 2504, 1154, 1022, 1565, 2895, 2620, 1853, 1300, 1074, 1310, 1893, 1533, 2747, 1069, 1084, 1009, 2618, 2730, 1490, 1058, 1210, 2131, 1180, 1308, 1588, 2944, 1156, 2388, 1384, 1108, 1082, 1126, 1143, 1032, 1468, 2413, 1150, 2350, 2512, 1587, 633, 2836, 1560, 1010, 1482, 1831, 2934, 3080, 1670, 1203, 1013, 1098, 1024, 1942, 1007, 5641, 2952, 1956, 2634, 1214, 2939, 1060, 1889, 2303, 1520, 2729, 1469, 3358, 1065, 1033, 3532, 2742, 1496, 2562, 2841, 732, 1181, 387, 1061, 1536, 1483, 1728, 1506, 1513, 1212, 1352, 2973, 1068, 2807, 1789, 1478, 1545, 1228, 1569, 1323, 2501, 1422, 2750, 1788, 1327, 1187, 6404, 1980, 1348, 2237, 1014, 1085, 1138, 1094, 2734, 2923, 1221, 1294, 1967, 1056, 2728, 1038, 630, 1307, 2524, 2970, 1627, 1607, 1107, 3100, 2736, 1915, 1879, 1144, 1102, 2935, 1119, 2961, 2898, 1004, 3220, 50, 2711, 1113, 1237, 2498, 1166, 1551, 1050, 3115, 1092, 2073, 1557, 1229, 1321, 1916, 1152, 2930, 3630, 2103, 2454, 2376, 1220, 1614, 1794, 1170, 1727, 2741, 1986, 1383, 2954, 2714, 1070, 3332, 1213, 1919, 1793, 1455, 1561, 2269, 1523, 1948, 2580, 2920, 2446, 2873, 3042, 1568, 1547, 1487, 1280, 1019, 1467, 2905, 1724, 3249, 1730, 2172, 2134, 1186, 2470, 727, 2495, 1184, 1556, 1620, 3306, 1985, 2743, 2949, 2132, 1748, 1402, 2749, 1924, 2555, 3308, 3262, 2254, 1200, 1856, 1162, 1580, 2967, 2362, 1055, 1223, 1264, 2278, 1328, 2543, 1371, 1463, 1494, 1054, 1169, 1209, 2964, 2320, 1215, 1176, 1199, 1089, 1191, 1075, 1376, 3221, 1153, 1249, 1522, 1163, 2616, 578, 1123, 1124, 1190]

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
