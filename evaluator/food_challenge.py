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
        VALID_CATEGORIES = [100022,100031,100049,100057,100059,100060,100063,100064,100067,100068,100069,100070,100072,100073,100076,100077,100078,100080,100082,100083,100084,100086,100089,100092,100093,100099,100101,100102,100104,100105,100107,100108,100111,100113,100114,100115,100123,100129,100130,100131,100132,100133,100135,100140,100141,100142,100143,100145,100146,100150,100151,100152,100156,100157,100158,100160,100161,100164,100171,100172,100173,100174,100175,100176,100177,100178,100179,100180,100181,100182,100183,100184,100185,100186,100190,100192,100195,100196,100200,100206,100224,100229,100234,100235,100243,100245,100249,100250,100264,100282,100300,100301,100302,100310,100314,100315,100318,100319,100321,100322,100324,100325,100332,100333,100334,100335,100337,100338,100346,100348,100349,100352,100355,100360,100364,100421,100423,100437,100442,100445,100456,100467,100475,100477,100486,100495,100523,100537,100546,100563,100594,100607,100645,100649,100652,100658,100674,100681,100687,100710,100719,100725,100742,100752,100757,100781,100790,100826,100834,100836,100838,100840,100842,100843,100844,100848,100859,100883,100895,100907,100909,100911,100916,100925,100926,100929,100936,100937,100942,100949,100951,100957,100958,100960,100962,100963,100966,100974,100978,100982,100992,100993,101006,101009,101012,101014,101022,101027,101029,101032,101038,101043,101077,101114,101118,101121,101123,101126,101129,101135,101138,101141,101144,101147,101148,101149,101150,101153,101156,101159,101164,101165,101166,101168,101170,101172,101173,101176,101177,101178,101180,101181,101182,101183,101185,101187,101188,101189,101190,101193,101194,101196,101197,101199,101200,101201,101208,101209,101210,101212,101213,101214,101215,101218,101219,101220,101228,101229,101231,101236,101237,101238,101240,101243,101244,101246,101247,101248,101249,101254,101255,101256,101257,101258,101260,101262,101265,101266,101268,101271,101272,101273,101274,101275,101279,101282,101283,101284,101285,101290,101291,101292,101294,101295,101296,101297,101298,101302,101303,101304,101305,101306,101307,101308,101309,101310,101311,101314,101317,101322,101323,101324,101325,101326,101327,101328,101329,101331,101335,101338,101340,101341,101343,101346,101347,101349,101354,101355,101358,101360,101361,101363,50]
        return VALID_CATEGORIES
