from predict_random import RandomPredictor

# Predictor which does nothing
random_predictor = RandomPredictor()

# UMX needs `models` folder to be present in your submission, check test_umx.py to learn more
# umx_predictor = UMXPredictor()

# X-UMX needs `models` folder to be present in your submission, check test_xumx.py to learn more
# xumx_predictor = XUMXPredictor()

# UMXL needs `models` folder to be present in your submission, check test_umxl.py to learn more
# Reminder: Set `external_dataset_used` to `true` in your `aicrowd.yaml` if your are using UMXL
# umxl_predictor = UMXLPredictor()

"""
PARTICIPANT_TODO: The implementation you want to submit as your submission
"""
submission = random_predictor
submission.run()
print("Successfully generated predictions...")
