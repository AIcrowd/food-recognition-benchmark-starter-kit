from evaluator.food_challenge import FoodChallengePredictor
import json
import numpy as np
import glob
import os
from PIL import Image


"""
Expected ENVIRONMENT Variables

* AICROWD_TEST_IMAGES_PATH : abs path to  folder containing all the test images
* AICROWD_PREDICTIONS_OUTPUT_PATH : path where you are supposed to write the output predictions.json
"""

# Configuration Variables

# List of valid categories to choose from
VALID_CATEGORIES = [2578, 1157, 2022, 1198, 2053, 1566, 2099, 1554, 1151, 2530, 2521, 2534, 1026, 1311, 2738, 1505, 1078, 1116, 1731, 1453, 1040, 1538, 2504, 1154, 1022, 1565, 2895, 2620, 1853, 1300, 1074, 1310, 1893, 1533, 2747, 1069, 1084, 1009, 2618, 2730, 1490, 1058, 1210, 2131, 1180, 1308, 1588, 2944, 1156, 2388, 1384, 1108, 1082, 1126, 1143, 1032, 1468, 2413, 1150, 2350, 2512, 1587, 633, 2836, 1560, 1010, 1482, 1831, 2934, 3080, 1670, 1203, 1013, 1098, 1024, 1942, 1007, 5641, 2952, 1956, 2634, 1214, 2939, 1060, 1889, 2303, 1520, 2729, 1469, 3358, 1065, 1033, 3532, 2742, 1496, 2562, 2841, 732, 1181, 387, 1061, 1536, 1483, 1728, 1506, 1513, 1212, 1352, 2973, 1068, 2807, 1789, 1478, 1545, 1228, 1569, 1323, 2501, 1422, 2750, 1788, 1327, 1187, 6404, 1980, 1348, 2237, 1014, 1085, 1138, 1094, 2734, 2923, 1221, 1294, 1967, 1056, 2728, 1038, 630, 1307, 2524, 2970, 1627, 1607, 1107, 3100, 2736, 1915, 1879, 1144, 1102, 2935, 1119, 2961, 2898, 1004, 3220, 50, 2711, 1113, 1237, 2498, 1166, 1551, 1050, 3115, 1092, 2073, 1557, 1229, 1321, 1916, 1152, 2930, 3630, 2103, 2454, 2376, 1220, 1614, 1794, 1170, 1727, 2741, 1986, 1383, 2954, 2714, 1070, 3332, 1213, 1919, 1793, 1455, 1561, 2269, 1523, 1948, 2580, 2920, 2446, 2873, 3042, 1568, 1547, 1487, 1280, 1019, 1467, 2905, 1724, 3249, 1730, 2172, 2134, 1186, 2470, 727, 2495, 1184, 1556, 1620, 3306, 1985, 2743, 2949, 2132, 1748, 1402, 2749, 1924, 2555, 3308, 3262, 2254, 1200, 1856, 1162, 1580, 2967, 2362, 1055, 1223, 1264, 2278, 1328, 2543, 1371, 1463, 1494, 1054, 1169, 1209, 2964, 2320, 1215, 1176, 1199, 1089, 1191, 1075, 1376, 3221, 1153, 1249, 1522, 1163, 2616, 578, 1123, 1124, 1190,]


class RandomPredictor(FoodChallengePredictor):

    """
    PARTICIPANT_TODO:
    You can do any preprocessing required for your codebase here like loading up models into memory, etc.
    """
    def prediction_setup(self):
        self.PADDING = 50
        self.SEGMENTATION_LENGTH = 10
        self.MAX_NUMBER_OF_ANNOTATIONS = 10

        pass

    """
    PARTICIPANT_TODO:
    During the evaluation all image file path will be provided one by one.

    NOTE: In case you want to load your model, please do so in `predict_setup` function.
    """
    def prediction(self, image_path):
        print("Generating for", image_path)
        annotations = []
        number_of_annotations = np.random.randint(0, self.MAX_NUMBER_OF_ANNOTATIONS)

        for _idx in range(number_of_annotations):
            _annotation = self.single_annotation(image_path)
            annotations.append(_annotation)

        # You can return single annotation or array of annotations in your code.
        return annotations

    """
    PARTICIPANT_TODO:
    You can define any custom function needed in this class, globally, or import from another file based on
    your convenience.
    Below are few helper functions needed by our random predictions generator
    """
    def bounding_box_from_points(self, points):
        """
        This function only supports the `poly` format.
        """
        points = np.array(points).flatten()
        even_locations = np.arange(points.shape[0] / 2) * 2
        odd_locations = even_locations + 1
        X = np.take(points, even_locations.tolist())
        Y = np.take(points, odd_locations.tolist())
        bbox = [X.min(), Y.min(), X.max() - X.min(), Y.max() - Y.min()]
        bbox = [int(b) for b in bbox]
        return bbox

    def single_segmentation(self, image_width, image_height, number_of_points=10):
        points = []
        for k in range(number_of_points):
            # Choose a random x-coordinate
            random_x = int(np.random.randint(0, image_width))
            # Choose a random y-coordinate
            random_y = int(np.random.randint(0, image_height))
            # Flatly append them to the list of points
            points.append(random_x)
            points.append(random_y)
        return [points]

    def single_annotation(self, image_path, number_of_points=10):
        width, height = self.get_image_width_height(image_path)
        _result = {"image_path": image_path}
        """
        Valid Categories are embedded in the annotations.json of the training set
        """
        _result["category_id"] = int(np.random.choice(VALID_CATEGORIES))

        _result["score"] = np.random.rand()  # a random score between 0 and 1

        _result["segmentation"] = self.single_segmentation(
            width, height, number_of_points=number_of_points
        )
        _result["bbox"] = self.bounding_box_from_points(_result["segmentation"])
        return _result

    def get_image_width_height(self, image_path):
        im = Image.open(image_path)
        width, height = im.size
        im.close()
        return width, height


if __name__ == "__main__":
    submission = RandomPredictor()
    submission.run()
    print("Successfully generated predictions!")
