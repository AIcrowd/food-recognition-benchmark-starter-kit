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

* [Dataset Utils](Dataset Utils.ipynb)
  * [Import Dependencies](Dataset Utils.ipynb#Import-dependencies)
  * [Configuration Variables](Dataset Utils.ipynb#Configuration-Variables)
  * [Parsing Annotations](Dataset Utils.ipynb#Parsing-the-annotations)
  * [Collecting and Visualizing Images](Dataset Utils.ipynb#Collecting-and-Visualizing-Images)
  * [Understanding Annotations](Dataset Utils.ipynb#Understanding-Annotations)
  * [Visualizing Annotations](Dataset Utils.ipynb#Visualizing-Annotations)
  * [Advanced](Dataset Utils.ipynb#Advanced)
    * [Convert poly segmentation to rle](Dataset Utils.ipynb#1)-Convert-poly-segmentation-to-rle)
    * [Convert segmentation to pixel level masks](Dataset Utils.ipynb#2)-Convert-segmentation-to-pixel-level-masks)
* [Random Submission](Random Submission.ipynb)
  * [Submission Format](Random Submission.ipynb#Submission-Format)
  * [Generating a Random Segmentation](Random Submission.ipynb#Generate-a-random-segmentation)
  * [Generating a Random Annotation Object](Random Submission.ipynb#Generate-a-random-annotation-object)
  * [Generating a Random Results Object](Random Submission.ipynb#Generate-a-results-object)
  * [Submit to crowdAI for grading](Random Submission.ipynb#Submit-to-crowdAI-for-grading)

```
python random_submission.py --api_key=<YOUR CROWDAI API KEY HERE>
```
* Train a Mask-RCNN
**TODO**

# Author   
Sharada Mohanty <sharada.mohanty@epfl.ch>
