#!/usr/bin/env python
import torch
import model
from dataset import MappingChallengeDataset
import evaluate
from config import Config

class MappingChallengeConfig(Config):
    """Configuration for training on MS COCO.
    Derives from the base Config class and overrides values specific
    to the COCO dataset.
    """
    # Give the configuration a recognizable name
    NAME = "crowdai-mapping-challenge"

    # Adjust down if you get an out of memory error
    IMAGES_PER_GPU = 20

    # Adjust to train on multiple GPUs
    GPU_COUNT = 2

    # DETECTION_MIN_CONFIDENCE = 0 # Use this only in Inference Mode

    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # The current version of the mapping-challenge dataset has only 1 class (Building) and one extra class for the background

    IMAGE_MIN_DIM = 320
    IMAGE_MAX_DIM = 320


config = MappingChallengeConfig()
print("BATCH SIZE ", config.BATCH_SIZE)

_model = model.MaskRCNN(config=config, model_dir="./logs")

if config.GPU_COUNT:
    _model = _model.cuda()

model_path="mask_rcnn_coco.pth"
_model.load_weights(model_path, ignore_layers=[
                                    "classifier.linear_class.weight",
                                    "classifier.linear_class.bias",
                                    "classifier.linear_bbox.weight",
                                    "classifier.linear_bbox.bias",
                                    "mask.conv5.weight",
                                    "mask.conv5.bias"
                                    ])


dataset_train = MappingChallengeDataset()
dataset_train.load_dataset(dataset_dir="data/train", load_small=True)
dataset_train.prepare()

dataset_val = MappingChallengeDataset()
val_coco = dataset_val.load_dataset(dataset_dir="data/val", load_small=True, return_coco=True)
dataset_val.prepare()

# evaluate.evaluate_coco(_model, dataset_val, val_coco, "segm")

# Training - Stage 1
print("Training network heads")
_model.train_model(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE,
            epochs=40,
            layers='heads')

# Training - Stage 2
# Finetune layers from ResNet stage 4 and up
print("Fine tune Resnet stage 4 and up")
_model.train_model(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE,
            epochs=120,
            layers='4+')

# Training - Stage 3
# Fine tune all layers
print("Fine tune all layers")
_model.train_model(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE / 10,
            epochs=160,
layers='all')
