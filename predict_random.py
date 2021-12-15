from evaluator.food_challenge import FoodChallengePredictor
import json
import glob
import os
import numpy as np
from PIL import Image


"""
Expected ENVIRONMENT Variables

* AICROWD_TEST_IMAGES_PATH : abs path to  folder containing all the test images
* AICROWD_PREDICTIONS_OUTPUT_PATH : path where you are supposed to write the output predictions.json
"""
class RandomPredictor(FoodChallengePredictor):

    """
    PARTICIPANT_TODO:
    You can do any preprocessing required for your codebase here like loading up models into memory, etc.
    """
    def prediction_setup(self):
        self.PADDING = 50
        self.SEGMENTATION_LENGTH = 10
        self.MAX_NUMBER_OF_ANNOTATIONS = 10
        pass

    """
    PARTICIPANT_TODO:
    During the evaluation all image file path will be provided one by one.

    NOTE: In case you want to load your model, please do so in `predict_setup` function.
    """
    def prediction(self, image_path):
        print("Generating for", image_path)
        annotations = []
        number_of_annotations = np.random.randint(0, self.MAX_NUMBER_OF_ANNOTATIONS)

        for _idx in range(number_of_annotations):
            _annotation = self.single_annotation(image_path)
            annotations.append(_annotation)

        # You can return single annotation or array of annotations in your code.
        return annotations

    """
    PARTICIPANT_TODO:
    You can define any custom function needed in this class, globally, or import from another file based on
    your convenience.
    Below are few helper functions needed by our random predictions generator
    """
    def bounding_box_from_points(self, points):
        """
        This function only supports the `poly` format.
        """
        points = np.array(points).flatten()
        even_locations = np.arange(points.shape[0] / 2) * 2
        odd_locations = even_locations + 1
        X = np.take(points, even_locations.tolist())
        Y = np.take(points, odd_locations.tolist())
        bbox = [X.min(), Y.min(), X.max() - X.min(), Y.max() - Y.min()]
        bbox = [int(b) for b in bbox]
        return bbox

    def single_segmentation(self, image_width, image_height, number_of_points=10):
        points = []
        for k in range(number_of_points):
            # Choose a random x-coordinate
            random_x = int(np.random.randint(0, image_width))
            # Choose a random y-coordinate
            random_y = int(np.random.randint(0, image_height))
            # Flatly append them to the list of points
            points.append(random_x)
            points.append(random_y)
        return [points]

    def single_annotation(self, image_path, number_of_points=10):
        width, height = self.get_image_width_height(image_path)
        _result = {"image_path": image_path}
        """
        Valid Categories are embedded in the annotations.json of the training set
        """
        _result["category_id"] = int(np.random.choice(self.valid_categories()))
        _result["score"] = np.random.rand()  # a random score between 0 and 1
        _result["segmentation"] = self.single_segmentation(
            width, height, number_of_points=number_of_points
        )
        _result["bbox"] = self.bounding_box_from_points(_result["segmentation"])
        return _result

    def get_image_width_height(self, image_path):
        im = Image.open(image_path)
        width, height = im.size
        im.close()
        return width, height


if __name__ == "__main__":
    submission = RandomPredictor()
    submission.run()
    print("Successfully generated predictions!")
