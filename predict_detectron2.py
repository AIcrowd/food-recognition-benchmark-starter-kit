#!/usr/bin/env python
#
# This file uses Detectron2 for instance segmentation.
# It is one of the official baselines for the Food Recognition benchmark 2022 challenge.
#
# NOTE: Detectron2 needs the model and **its** aicrowd.json file to be submitted along with your code.
#
# Making submission using Detectron2:
# 1. Copy the aicrowd_detectron2.json from utils to home directory:
#    #> cp utils/aicrowd_detectron2_example.json aicrowd.json
# 2. Change the model in `predict.py` to Detectron2Predictor.
# 3. Download the pre-trained model from google drive into the folder `./models` using:
#    #> mkdir models
#    #> cd models
#    #> pip install gdown
#    #> gdown --id 1ylaOzaI6qBfZbICA844uD74dKxLwcd0K --output model_final.pth
# 3. Submit your code using git-lfs
#    #> git lfs install
#    #> git lfs track "*.pth"
#    #> git add .gitattributes
#    #> git add models
#

import os
import json
import glob
from PIL import Image
import importlib
import numpy as np
import cv2
import torch

import pycocotools.mask as mask_util
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.structures import Boxes, BoxMode

from detectron2.data import build_detection_test_loader
from detectron2.evaluation import COCOEvaluator, inference_on_dataset

from evaluator.food_challenge import FoodChallengePredictor


"""
Expected ENVIRONMENT Variables
* AICROWD_TEST_IMAGES_PATH : abs path to  folder containing all the test images
* AICROWD_PREDICTIONS_OUTPUT_PATH : path where you are supposed to write the output predictions.json
"""

class Detectron2Predictor(FoodChallengePredictor):

    """
    PARTICIPANT_TODO:
    You can do any preprocessing required for your codebase here like loading up models into memory, etc.
    """
    def prediction_setup(self):
        # self.PADDING = 50
        # self.SEGMENTATION_LENGTH = 10
        # self.MAX_NUMBER_OF_ANNOTATIONS = 10

        #set the config parameters, including the architecture which was previously used
        self.config = self.get_detectron_config()
        self.model_name = self.config["model_type"]
        self.model = importlib.import_module(f"detectron2.{self.model_name}")
        self.class_to_category = self.get_class_to_category()

        self.cfg = get_cfg()
        self.cfg.merge_from_file(self.model.get_config_file(self.config["model_config_file"]))
        self.cfg.MODEL.WEIGHTS = self.config["model_path"]

        #set the threshold & num classes
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.config["detectron_model_config"]["ROI_HEADS"]["SCORE_THRESH_TEST"]   # set the testing threshold for this model
        self.cfg.MODEL.ROI_HEADS.NUM_CLASSES = 498

        self.cfg.MODEL.DEVICE = "cuda"
        self.predictor = DefaultPredictor(self.cfg)


    """
    PARTICIPANT_TODO:
    During the evaluation all image file path will be provided one by one.
    NOTE: In case you want to load your model, please do so in `predict_setup` function.
    """
    def prediction(self, image_path):
        print("Generating for", image_path)
        # read the image
        img = cv2.imread(image_path)
        prediction = self.predictor(img)
        
        annotations = []
        instances = prediction["instances"]
        if len(instances) > 0:
            scores = instances.scores.tolist()
            classes = instances.pred_classes.tolist()
            bboxes = BoxMode.convert(
                instances.pred_boxes.tensor.cpu(),
                BoxMode.XYXY_ABS,
                BoxMode.XYWH_ABS,
            ).tolist()

            masks = []
            if instances.has("pred_masks"):
                for mask in instances.pred_masks.cpu():
                    _mask = mask_util.encode(np.array(mask[:, :, None], order="F", dtype="uint8"))[0]
                    _mask["counts"] = _mask["counts"].decode("utf-8")
                    masks.append(_mask)

            for idx in range(len(instances)):
                category_id = self.class_to_category[str(classes[idx])] # json converts int keys to str
                output = {
                    "image_id": int(os.path.basename(image_path).split(".")[0]),
                    "category_id": category_id,
                    "bbox": bboxes[idx],
                    "score": scores[idx],
                }
                if len(masks) > 0:
                    output["segmentation"] = masks[idx]
                annotations.append(output)
        
        # You can return single annotation or array of annotations in your code.
        return annotations

    def get_class_to_category(self):
        class_to_category = {}
        with open("class_to_category.json") as fp:
            class_to_category = json.load(fp)
        return class_to_category

    def get_detectron_config(self):
        with open("aicrowd.json") as fp:
            config = json.load(fp)
        return config


if __name__ == "__main__":
    submission = Detectron2Predictor()
    submission.run()
    print("Successfully generated predictions!")
