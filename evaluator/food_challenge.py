######################################################################################
### This is a read-only file to allow participants to run their code locally.      ###
### It will be over-writter during the evaluation, Please do not make any changes  ###
### to this file.                                                                  ###
######################################################################################

import os
import glob
import json
import traceback
from evaluator.utils import time_limit


class FoodChallengePredictor:
    def __init__(self):
        self.test_data_path = os.getenv("TEST_DATASET_PATH", os.getcwd() + "/data/test/")
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
            self.predictions.append(prediction)

        self.update_status_to_evaluation_system("Predictions generated")
        self.save_predictions()

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

    def scoring(self):
        """
        Add scoring function in the starter kit for participant's reference
        """
        raise NotImplementedError
