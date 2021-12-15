######################################################################################
### This is a read-only file to allow participants to run their code locally.      ###
### It will be over-writter during the evaluation, Please do not make any changes  ###
### to this file.                                                                  ###
######################################################################################

import os
import glob
import json
import traceback
import numpy as np
import pandas as pd
from evaluator.utils import time_limit
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


class FoodChallengePredictor:
    def __init__(self):
        self.test_data_path = os.getenv("TEST_DATASET_PATH", os.getcwd() + "/data/images/")
        self.results_data_path = os.getenv("RESULTS_DATASET_PATH", os.getcwd() + "/data/results/")
        self.prediction_setup_timeout = int(os.getenv("PREDICTION_SETUP_TIMEOUT_SECONDS", "120"))
        self.prediction_per_image_timeout = int(os.getenv("PREDICTION_PER_IMAGE_TIMEOUT_SECONDS", "1"))
        self.is_online_run = False
        self.predictions = []

    def get_all_image_paths(self):
        return glob.glob(os.path.join(self.test_data_path, "*.jpg"))

    def update_status_to_evaluation_system(self, message):
        pass

    def evaluation(self):
        """
        Admin function: Runs the whole evaluation
        """
        self.update_status_to_evaluation_system("Running prediction_setup")
        try:
            with time_limit(self.prediction_setup_timeout):
                self.prediction_setup()
            self.update_status_to_evaluation_system("Completed prediction_setup")
        except NotImplementedError:
            self.update_status_to_evaluation_system("prediction_setup doesn't exist for this run, skipping...")

        image_paths = self.get_all_image_paths()

        for image_path in image_paths:
            with time_limit(self.prediction_per_image_timeout):
                prediction = self.prediction(image_path=image_path)
            if isinstance(prediction, (list, pd.core.series.Series, np.ndarray)):
                for i in prediction:
                    self.add_prediction(i)
            else:
                self.add_prediction(prediction)

        self.update_status_to_evaluation_system("Predictions generated")
        self.save_predictions()

    def add_prediction(self, prediction):
        if 'image_id' not in prediction:
            prediction['image_id'] = int(os.path.splitext(os.path.basename(prediction['image_path']))[0])
        self.validate_prediction(prediction)
        self.predictions.append(prediction)

    def validate_prediction(self, prediction):
        assert prediction['image_id'] is not None
        assert prediction['category_id'] is not None and prediction['category_id'] in self.valid_categories()
        assert prediction['score'] is not None and 0.0 <= prediction['score'] <= 1.0
        assert prediction['segmentation'] is not None
        assert prediction['bbox'] is not None

    def save_predictions(self):
        fp = open(os.path.join(self.results_data_path, 'predictions.json'), 'w')
        fp.write(json.dumps(self.predictions))
        fp.close()

    def run(self):
        try:
            self.evaluation()
        except Exception as e:
            error = traceback.format_exc()
            print(error)
            if self.is_online_run:
                raise e

    def prediction_setup(self):
        """
        You can do any preprocessing required for your codebase here : 
            like loading your models into memory, etc.
        """
        raise NotImplementedError

    def prediction(self, image_path):
        """
        This function will be called for all the images one by one during the evaluation.
        NOTE: In case you want to load your model, please do so in `prediction_setup` function.
        """
        raise NotImplementedError

    def _report(self, message):
        print(message)

    def scoring(self, ground_truth_path, predictions_file_path):
        if not os.path.exists(predictions_file_path):
            raise Exception(
                "Invalid predictions_file_path provided : ".format(predictions_file_path)
            )

        self._report("Loading Ground Truth Annotations...")
        ground_truth_annotations = COCO(ground_truth_path)

        self._report("Loading Predicted Annotations from : {}".format(predictions_file_path))
        predictions = json.loads(open(predictions_file_path).read())
        self._report("Predictions JSON read into memoery...")
        assert (
            len(predictions) > 0
        ), "Predictions JSON file should have atleast 1 annotation"

        self._report("Parsing Predictions......")
        print("Length of annotations : ", len(predictions))
        print("Ground truth File PATH : ", ground_truth_path)
        print("Predictions File Path : ", predictions_file_path)

        results = ground_truth_annotations.loadRes(predictions)
        self._report("Predicted Annotations Loaded Successfully...")

        self._report("Initiating evaluation. This might take a few minutes. Hang in there :D ")
        cocoEval = COCOeval(ground_truth_annotations, results, "segm")
        cocoEval.evaluate()

        self._report("Accumulating evaluation results....")
        cocoEval.accumulate()
        cocoEval.summarize()
        _result_object = {
            "score": cocoEval.stats[0],
            "score_secondary": cocoEval.stats[8],
            "meta": {
                "average_precision_iou_all_area_all_max_dets_100": cocoEval.stats[0],
                "average_precision_iou_5_area_all_max_dets_100": cocoEval.stats[1],
                "average_precision_iou_75_area_all_max_dets_100": cocoEval.stats[2],
                "average_precision_iou_all_area_small_max_dets_100": cocoEval.stats[3],
                "average_precision_iou_all_area_medium_max_dets_100": cocoEval.stats[4],
                "average_precision_iou_all_area_large_max_dets_100": cocoEval.stats[5],
                "average_recall_iou_all_area_all_max_dets_1": cocoEval.stats[6],
                "average_recall_iou_all_area_all_max_dets_10": cocoEval.stats[7],
                "average_recall_iou_all_area_all_max_dets_100": cocoEval.stats[8],
                "average_recall_iou_all_area_small_max_dets_1": cocoEval.stats[9],
                "average_recall_iou_all_area_medium_max_dets_1": cocoEval.stats[10],
                "average_recall_iou_all_area_large_max_dets_1": cocoEval.stats[11],
            }
        }
        return _result_object

    def valid_categories(self):
        # List of valid categories to choose from
        # Description of categories is present in annotations.json file as part of dataset
        VALID_CATEGORIES = [50, 143, 158, 198, 232, 236, 259, 281, 282, 387, 483, 578, 629, 630, 633, 656, 727, 732, 733, 752, 780, 843, 870, 922, 929, 1004, 1007, 1009, 1010, 1013, 1014, 1019, 1020, 1021, 1022, 1024, 1026, 1032, 1033, 1038, 1040, 1050, 1054, 1055, 1056, 1058, 1060, 1061, 1062, 1065, 1068, 1069, 1070, 1074, 1075, 1076, 1078, 1082, 1084, 1085, 1086, 1089, 1090, 1091, 1092, 1093, 1094, 1098, 1102, 1107, 1108, 1111, 1112, 1113, 1115, 1116, 1119, 1120, 1121, 1123, 1124, 1125, 1126, 1130, 1134, 1138, 1141, 1143, 1144, 1150, 1151, 1152, 1153, 1154, 1156, 1157, 1158, 1162, 1163, 1164, 1166, 1167, 1169, 1170, 1174, 1175, 1176, 1180, 1181, 1184, 1186, 1187, 1190, 1191, 1198, 1199, 1200, 1201, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1218, 1219, 1220, 1221, 1222, 1223, 1228, 1229, 1237, 1249, 1253, 1256, 1257, 1264, 1266, 1280, 1282, 1290, 1293, 1294, 1295, 1300, 1307, 1308, 1309, 1310, 1311, 1321, 1323, 1325, 1327, 1328, 1337, 1346, 1348, 1352, 1366, 1367, 1371, 1376, 1383, 1384, 1402, 1411, 1422, 1453, 1454, 1455, 1456, 1463, 1467, 1468, 1469, 1471, 1478, 1479, 1482, 1483, 1487, 1488, 1490, 1492, 1494, 1496, 1500, 1505, 1506, 1509, 1513, 1517, 1520, 1522, 1523, 1528, 1533, 1536, 1538, 1545, 1546, 1547, 1551, 1554, 1556, 1557, 1559, 1560, 1561, 1565, 1566, 1568, 1569, 1572, 1580, 1584, 1587, 1588, 1592, 1595, 1607, 1612, 1614, 1615, 1616, 1620, 1626, 1627, 1670, 1695, 1696, 1707, 1711, 1724, 1725, 1727, 1728, 1730, 1731, 1748, 1749, 1757, 1760, 1765, 1770, 1788, 1789, 1791, 1793, 1794, 1831, 1835, 1837, 1838, 1845, 1849, 1853, 1856, 1857, 1879, 1883, 1886, 1889, 1893, 1895, 1908, 1914, 1915, 1916, 1917, 1919, 1924, 1942, 1948, 1956, 1958, 1967, 1975, 1980, 1985, 1986, 2002, 2003, 2022, 2031, 2053, 2056, 2062, 2073, 2099, 2103, 2113, 2115, 2131, 2132, 2133, 2134, 2135, 2171, 2172, 2184, 2194, 2203, 2211, 2237, 2254, 2259, 2262, 2269, 2278, 2300, 2303, 2312, 2320, 2333, 2340, 2350, 2355, 2362, 2376, 2388, 2395, 2400, 2408, 2413, 2446, 2452, 2454, 2461, 2467, 2468, 2470, 2495, 2498, 2501, 2504, 2512, 2513, 2518, 2521, 2524, 2530, 2534, 2543, 2546, 2548, 2553, 2555, 2562, 2563, 2577, 2578, 2580, 2585, 2588, 2605, 2607, 2610, 2616, 2618, 2620, 2634, 2636, 2711, 2714, 2716, 2718, 2719, 2728, 2729, 2730, 2731, 2734, 2736, 2738, 2740, 2741, 2742, 2743, 2744, 2747, 2749, 2750, 2751, 2752, 2760, 2767, 2768, 2773, 2778, 2791, 2807, 2810, 2811, 2815, 2836, 2837, 2840, 2841, 2846, 2852, 2855, 2859, 2873, 2895, 2896, 2898, 2899, 2900, 2905, 2906, 2913, 2918, 2920, 2923, 2930, 2932, 2934, 2935, 2939, 2941, 2944, 2947, 2949, 2952, 2954, 2959, 2960, 2961, 2962, 2964, 2966, 2967, 2968, 2970, 2973, 2990, 2991, 2994, 3042, 3046, 3055, 3080, 3082, 3085, 3100, 3101, 3115, 3181, 3220, 3221, 3228, 3230, 3248, 3249, 3258, 3262, 3293, 3306, 3308, 3332, 3337, 3358, 3392, 3399, 3415, 3416, 3417, 3474, 3532, 3615, 3630, 3739, 4335, 4338, 5247, 5618, 5641, 5689, 5748, 5792, 5812, 6404, 7504, 8025, 8730, 9594, 10626]
        return VALID_CATEGORIES