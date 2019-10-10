# food-recognition-challenge-starter-kit
![AIcrowd-Logo](https://raw.githubusercontent.com/AIcrowd/AIcrowd/master/app/assets/images/misc/aicrowd-horizontal.png)


# Installation
```
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit
pip install  awscli botocore certifi cffi colorama cycler Cython decorator jmespath kiwisolver matplotlib networkx numpy olefile Pillow pyasn1 pycparser pyparsing python-dateutil pytz PyWavelets rsa s3transfer scikit-image scipy six tqdm jupyter-client jupyter-console jupyter-core jupyter-repo2docker jupyterlab jupyterlab-launcher crowdai
pip install pip install git+https://github.com/AIcrowd/coco.git#subdirectory=PythonAPI
```

# Dataset
Please download the datasets from [https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files](https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files](https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files](https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files), and put them in the `data/` folder. [Untar](http://how-to.wikia.com/wiki/How_to_untar_a_tar_file_or_gzip-bz2_tar_file) them (this might take some time) to have the following directory structure:

```bash
|-- data/
|   |-- test_images/ (has all images for prediction)
|   |-- train/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |-- val/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
```

# Usage
Now you can refer to the list of Jupyter Notebooks for different aspects of the challenge and the datasets.
You can access all of them by :
```bash
jupyter-notebook
```
## Available Notebooks

* [Dataset Utils](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb)
  * [Import Dependencies](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Import-dependencies)
  * [Configuration Variables](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Configuration-Variables)
  * [Parsing Annotations](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Parsing-the-annotations)
  * [Collecting and Visualizing Images](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Collecting-and-Visualizing-Images)
  * [Understanding Annotations](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Understanding-Annotations)
  * [Visualizing Annotations](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Visualizing-Annotations)
  * [Advanced](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#Advanced)
    * [Convert poly segmentation to rle](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#1.-Convert-poly-segmentation-to-rle)
    * [Convert segmentation to pixel level masks](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Dataset%20Utils.ipynb#2.-Convert-segmentation-to-pixel-level-masks)
* [Random Submission](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/run.py)
* [Locally test the evaluation function](https://github.com/AIcrowd/food-recognition-challenge-starter-kit/blob/master/Local%20Evaluation.ipynb)   

## Miscelaneous Resources
* [Convert Annotations from MS COCO format to PascalVOC format](https://github.com/CasiaFan/Dataset_to_VOC_converter/blob/master/anno_coco2voc.py)

# Author   
**[Sharada Mohanty](https://twitter.com/memohanty?lang=en)**
