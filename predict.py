from predict_random import RandomPredictor

# Predictor which does nothing
random_predictor = RandomPredictor()

# mmdetection needs `models` folder to be present in your submission, check predict_mmdetection.py to learn more
# mmdetection_predictor = MMDetectionPredictor()

# maskrcnn needs `models` folder to be present in your submission, check predict_maskrcnn.py to learn more
# maskrcnn_predictor = MaskRCNNPredictor()

"""
PARTICIPANT_TODO: The implementation you want to submit as your submission
"""
submission = random_predictor
submission.run()
print("Successfully generated predictions...")
