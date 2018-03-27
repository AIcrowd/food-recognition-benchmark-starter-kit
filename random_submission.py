import random
import json
import numpy as np
import argparse

results = []

IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
padding = 50
SEGMENTATION_LENGTH = 10

IMAGE_IDS = list(range(60697)) #As there are 60582, and the image_ids are sequentially numbered

print("Generating random results file....")
for k in IMAGE_IDS:
    _result = {}
    _result["image_id"] = k
    _result["category_id"] = 100 # Category ID for "Building"
    _result["score"] = np.random.rand()
    x = random.randint(0, IMAGE_WIDTH-padding)
    y = random.randint(0, IMAGE_HEIGHT-padding)
    width = random.randint(0, IMAGE_WIDTH-x)
    height = random.randint(0, IMAGE_WIDTH-y)
    _result["bbox"] = [x, y, width, height]

    _segmentation=[]
    for k in range(SEGMENTATION_LENGTH*2):
        _segmentation.append(np.random.randint(0, IMAGE_WIDTH))
        _segmentation.append(np.random.randint(0, IMAGE_HEIGHT))
    _result["segmentation"] = [_segmentation]

    results.append(_result)

print("Writing results to : data/result_annotations.json")
with open("data/result_annotations.json", "w") as fp:
    fp.write(json.dumps(results))
print("Writing Complete !")

print("Submitting to crowdAI...")

parser = argparse.ArgumentParser(description='Submit the result to crowdAI')
parser.add_argument('--api_key', dest='api_key', action='store', required=True)
args = parser.parse_args()

import crowdai
api_key = args.api_key
challenge = crowdai.Challenge("crowdAIMappingChallenge", api_key)
result = challenge.submit("data/result_annotations.json")
print(result)
