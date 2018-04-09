# mapping-challenge-starter-kit
![CrowdAI-Logo](https://github.com/crowdAI/crowdai/raw/master/app/assets/images/misc/crowdai-logo-smile.svg?sanitize=true)

[![gitter-badge](https://badges.gitter.im/crowdAI/crowdai-mapping-challenge.png)](https://gitter.im/crowdAI/crowdai-mapping-challenge)

# Installation
```
git clone https://github.com/crowdAI/mapping-challenge-starter-kit
cd mapping-challenge-starter-kit
pip install -r requirements.txt
```

# Dataset
Please download the datasets from [https://www.crowdai.org/challenges/mapping-challenge/dataset_files](https://www.crowdai.org/challenges/mapping-challenge/dataset_files), and put them in the `data/` folder. [Untar](http://how-to.wikia.com/wiki/How_to_untar_a_tar_file_or_gzip-bz2_tar_file) them (this might take some time) to have the following directory structure:

```bash
|-- data/
|   |-- test_images/ (has all images for prediction)
|   |-- train/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the "annotation.json"
|   |-- val/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the "annotation.json"
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

* [Locally test the evaluation function](https://github.com/crowdAI/mapping-challenge-starter-kit/blob/master/Local%20Evaluation.ipynb)   

* Train [Mask-RCNN](https://arxiv.org/abs/1703.06870)
  * [Installation](https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn)
  * [Training](https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn/blob/master/Training.ipynb)
  * [Prediction & Submission](https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn/blob/master/Prediction-and-Submission.ipynb)
  * **NOTE** : This is in a separate repository, and we have also now added the pretrained weights from the baseline submission to the [datasets page](https://www.crowdai.org/challenges/mapping-challenge/dataset_files).

## Miscelaneous Resources
* [Convert Annotations from MS COCO format to PascalVOC format](https://github.com/CasiaFan/Dataset_to_VOC_converter/blob/master/anno_coco2voc.py)

# Acknowledgements  
A big shout out to our awesome community members [@MasterScat (Florian Laurent)](https://www.crowdai.org/participants/masterscrat), [Snigdha Dagar](snigdha.dagar@gmail.com), and [Iuliana Voinea](https://www.crowdai.org/participants/iuliana), for their help in preparing the datasets and designing the challenge.


# Author   
Sharada Mohanty <sharada.mohanty@epfl.ch>
