import os
from evaluator.food_challenge import FoodChallengePredictor

submission = FoodChallengePredictor()

# Put your predictions file path [to override default one]
predictions_file_path = os.path.join(submission.results_data_path, 'predictions.json')

# Ground truth file path [depending on how you export the dataset]
ground_truth_path = "data/annotations.json"

result_object = submission.scoring(ground_truth_path, predictions_file_path)

print("""Scores Computed!!\n \
Mean Average Precision : {}\n \
Mean Average Recall : {}\n \
All Scores: {}""".format(
    result_object["score"], result_object["score_secondary"], result_object["meta"]
))