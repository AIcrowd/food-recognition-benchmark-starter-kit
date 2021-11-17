from evaluator.food_challenge import FoodChallengePredictor

print("Calculating scores for local run...")
submission = FoodChallengePredictor()
scores = submission.scoring()
print(scores)
