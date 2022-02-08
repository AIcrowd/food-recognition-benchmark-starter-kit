# from predict_random import RandomPredictor
from predict_detectron2 import Detectron2Predictor
from predict_mmdetection import MMDetectionPredictor

# Predictor which does nothing
# random_predictor = RandomPredictor()

# mmdetection needs `models` folder to be present in your submission, check predict_mmdetection.py to learn more
mmdetection_predictor = MMDetectionPredictor()

# maskrcnn needs `models` folder to be present in your submission, check predict_maskrcnn.py to learn more
# maskrcnn_predictor = MaskRCNNPredictor()

#Detectron2 needs `models` folder to be present in your submission, check predict_detectron2.py to learn more
detectron2_predictor = Detectron2Predictor()

# Your own implementation
# my_predictor = MyPredictor()


"""
PARTICIPANT_TODO: The implementation you want to submit as your submission
"""
submission = mmdetection_predictor
submission.run()
print("Successfully generated predictions...")
