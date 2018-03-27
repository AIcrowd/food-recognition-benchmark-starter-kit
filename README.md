# mapping-challenge-starter-kit


# Installation
```
git clone git@github.com:crowdAI/mapping-challenge-starter-kit.git
cd mapping-challenge-starter-kit
pip install -r requirements.txt
```
**Note** : The dependencies of [PyTorch](http://pytorch.org/) have been commented out from the `requirements.txt` file, and please install the same by following the instructions here : [http://pytorch.org/](http://pytorch.org/).

# Dataset
Please download the datasets from [https://www.crowdai.org/challenges/mapping-challenge/dataset_files](https://www.crowdai.org/challenges/mapping-challenge/dataset_files), and untar them to have the following directory structure :

```bash
|-- data
|   |-- test_images (has all images for prediction)
|   |-- train
|   |   `-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
|   `-- val
|   |   `-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
```

# Usage
**TODO** Add more description
* Random Submission
```
python random_submission.py --api_key=<YOUR CROWDAI API KEY HERE>
```
* Train a Mask-RCNN
**TODO**

# Author   
Sharada Mohanty <sharada.mohanty@epfl.ch>
