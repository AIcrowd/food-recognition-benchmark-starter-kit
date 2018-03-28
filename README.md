# mapping-challenge-starter-kit
![CrowdAI-Logo](https://github.com/crowdAI/crowdai/raw/master/app/assets/images/misc/crowdai-logo-smile.svg?sanitize=true)

# Installation
```
git clone git@github.com:crowdAI/mapping-challenge-starter-kit.git
cd mapping-challenge-starter-kit
pip install -r requirements.txt
```

# Dataset
Please download the datasets from [https://www.crowdai.org/challenges/mapping-challenge/dataset_files](https://www.crowdai.org/challenges/mapping-challenge/dataset_files), and untar them to have the following directory structure :

```bash
|-- data/
|   |-- test_images/ (has all images for prediction)
|   |-- train/
|   |   `-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
|   `-- val/
|   |   `-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
```

# Usage
Now you can refer to the list of Jupyter Notebooks for different aspects of the challenge and the datasets.
You can access all of them by :
```bash
jupyter-notebook
```
## Available Notebooks

* [Dataset Utils](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb)
  * [Import Dependencies](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Import-dependencies)
  * [Configuration Variables](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Configuration-Variables)
  * [Parsing Annotations](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Parsing-the-annotations)
  * [Collecting and Visualizing Images](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Collecting-and-Visualizing-Images)
  * [Understanding Annotations](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Understanding-Annotations)
  * [Visualizing Annotations](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Visualizing-Annotations)
  * [Advanced](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Advanced)
    * [Convert poly segmentation to rle](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#1.-Convert-poly-segmentation-to-rle)
    * [Convert segmentation to pixel level masks](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#2.-Convert-segmentation-to-pixel-level-masks)
* [Random Submission](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb)
  * [Submission Format](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Submission-Format)
  * [Generating a Random Segmentation](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Generate-a-random-segmentation)
  * [Generating a Random Annotation Object](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Generate-a-random-annotation-object)
  * [Generating a Random Results Object](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Generate-a-results-object)
  * [Submit to crowdAI for grading](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Random%20Submission.ipynb#Submit-to-crowdAI-for-grading)
* Train [Mask-RCNN](https://arxiv.org/abs/1703.06870) : `Coming Soon`

# Author   
Sharada Mohanty <sharada.mohanty@epfl.ch>
