# Food Recognition Challenge - Starter Kit

![Food-Challenge](https://i.imgur.com/0G3PEc7.png)


- 💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/food-recognition-challenge
- 🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/food-recognition-challenge/discussion
- 🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/food-recognition-challenge/leaderboards

<p align="center">
 <a href="https://discord.gg/GTckBMx"><img src="https://img.shields.io/discord/657211973435392011?style=for-the-badge" alt="chat on Discord"></a>
</p>


# 🕵️ Problem Statement

The goal of this challenge is to train models which can look at images of food items and detect the individual food items present in them.
We provide a novel dataset of food images collected using the MyFoodRepo project where numerous volunteer Swiss users provide images of their daily food intake. The images have been hand labelled by a group of experts to map the individual food items to an ontology of Swiss Food items.

This is an evolving dataset, where we will release more data as the dataset grows in size.

![image1](https://i.imgur.com/zS2Nbf0.png)


# 💻 Installation

Ensure you have `docker` and `nvidia-docker` installed by following the instructions here : 

* [Docker](https://docs.docker.com/install/)
* [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
**NOTE** : You do not need nvidia-docker if you do not want to use GPU when testing your submission locally

```
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit
pip3 install -r requirements.txt
pip3 install git+https://github.com/AIcrowd/coco.git
```

# 💾 Dataset

The dataset for the [AIcrowd Food Recognition Challenge](https://www.aicrowd.com/challenges/food-recognition-challenge) is available at [https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files](https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files)

This dataset contains :   
* `train-v0.4.tar.gz` : This is the Training Set of **24120** (as RGB images) food images, along with their corresponding **39328** annotations in [MS-COCO format](http://cocodataset.org/#home)

* `val-v0.4.tar.gz`: This is the suggested Validation Set of **1269** (as RGB images) food images, along with their corresponding **2053** annotations in [MS-COCO format](http://cocodataset.org/#home)

* `test_images-v0.4.tar.gz` : This is the debug Test Set for Round-3, where you are provided the same images as the validation set.

To get started, we would advise you to download all the files, and untar them inside the `data/` folder of this repository, so that you have a directory structure like this : 

```bash
|-- data/
|   |-- test_images/ (has all images for prediction)(**NOTE** : They are the same as the validation set images)
|   |-- train/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
|   |-- val/
|   |   |-- images (has all the images for training)
|   |   |__ annotation.json : Annotation of the data in MS COCO format
|   |   |__ annotation-small.json : Smaller version of the previous dataset
```

We are also assuming that you have already installed all the requirements for this notebook, or you can still install them by :


```

# Usage
Now you can refer to the list of Jupyter Notebooks for different aspects of the challenge and the datasets.
You can access all of them by :
```bash
jupyter-notebook
```

![image](https://i.imgur.com/EWIuxYR.png)

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

# 📚 Baselines
## Round 1
* [Colab Notebook for Data Analysis and Tutorial](https://colab.research.google.com/drive/1A5p9GX5X3n6OMtLjfhnH6Oeq13tWNtFO#scrollTo=ok54AWT_VoWV)
A notebook with data analysis on the Food Recognition Dataset and then a short tutorial on training with keras and pytorch. This lets you immediately jump onto the challenge and solve the challenge
### Pretrained Baselines
* [mmdetection (pytorch)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-pytorch-baseline)  
* [matterport-maskrcnn (keras - tensorflow)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-recognition)

## Round 2
* [Colab Notebook for Data Analysis and Tutorial](https://colab.research.google.com/drive/1vXdv9quZ7CXO5lLCjhyz3jtejRzDq221)
A notebook with data analysis on the Food Recognition Dataset and then a short tutorial on training with keras and pytorch. This lets you immediately jump onto the challenge and solve the challenge
### Pretrained Baselines
* [mmdetection (pytorch)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-round2) 

## Round 3
* Cooking right now!! 🍳  Coming soon 😉

# 🖊 Evaluation Criteria

For for a known ground truth mask **A**, you propose a mask **B**, then we first compute **IoU** (Intersection Over Union) :      

<img src="https://latex.codecogs.com/svg.latex?IoU(A,B)=\frac{A{\cap}B}{A{\cup}B}" title="$$ IoU(A, B) = \frac{A \cap B}{ A \cup B} $$" />

$$IoU$$ measures the overall overlap between the true region and the proposed region.
Then we consider it a True detection, when there is atleast half an overlap, or when **IoU > 0.5**

Then we can define the following parameters :

* Precision (**IoU > 0.5**)   
<img src="https://latex.codecogs.com/svg.latex?P_{IoU\geq0.5}=\frac{TP_{IoU\geq0.5}}{TP_{IoU\geq0.5}+FP_{IoU\geq0.5}}" title="$$ P_{IoU \geq 0.5} = \frac{TP_{IoU \geq 0.5}}{TP_{IoU \geq 0.5} + FP_{IoU \geq 0.5}} $$" />

* Recall (**IoU > 0.5**)   
<img src="https://latex.codecogs.com/gif.latex?$$&space;R_{IoU&space;\geq&space;0.5}&space;=&space;\frac{TP_{IoU&space;\geq&space;0.5}}{TP_{IoU&space;\geq&space;0.5}&space;&plus;&space;FN_{IoU&space;\geq&space;0.5}}&space;$$." title="$$ R_{IoU \geq 0.5} = \frac{TP_{IoU \geq 0.5}}{TP_{IoU \geq 0.5} + FN_{IoU \geq 0.5}} $$." />

The final scoring parameters **AP_{IoU > 0.5}** and **AR_{IoU > 0.5}** are computed by averaging over all the precision and recall values for all known annotations in the ground truth.


# 🚀 Submission Instructions

To submit to the challenge you'll need to ensure you've set up an appropriate repository structure, create a private git repository at https://gitlab.aicrowd.com with the contents of your submission, and push a git tag corresponding to the version of your repository you'd like to submit.

## Repository Structure
We have created this sample submission repository which you can use as reference.

#### aicrowd.json
Each repository should have a aicrowd.json file with the following fields:

```
{
    "challenge_id" : "aicrowd-food-recognition-challenge",
    "grader_id": "aicrowd-food-recognition-challenge",
    "authors" : ["aicrowd-user"],
    "description" : "Food Recognition Challenge Submission",
    "license" : "MIT",
    "gpu": false
}
```
This file is used to identify your submission as a part of the Food Recognition Challenge.  You must use the `challenge_id` and `grader_id` specified above in the submission. The `gpu` key in the `aicrowd.json` lets your specify if your submission requires a GPU or not. In which case, a NVIDIA-K80 will be made available to your submission when evaluation the submission.

#### Submission environment configuration
You can specify the software runtime of your code by modifying the included [Dockerfile](Dockerfile). 

#### Code Entrypoint
The evaluator will use `/home/aicrowd/run.sh` as the entrypoint. Please remember to have a `run.sh` at the root which can instantiate any necessary environment variables and execute your code. This repository includes a sample `run.sh` file.

### Local Debug

```
export TEST_IMAGES_PATH="./data/test_images"
export IMAGE_NAME="aicrowd-food-recognition-challenge-submission"

./build.sh
./debug.sh

######################################
## NOTE : 
## 
## * If you do not wish to your a GPU when testing locally, please feel free to replace nvidia-docker with docker
##
## * If you want to test on images located at an alternate location, set the `TEST_IMAGES_PATH` environment variable accordingly before running `build.sh` and `debug.sh`.
```

### Submitting 

#### Using SSH
To make a submission, you will have to create a private repository on [https://gitlab.aicrowd.com](https://gitlab.aicrowd.com).

You will have to add your SSH Keys to your GitLab account by following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).
If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/ssh/README.html#generating-a-new-ssh-key-pair).

*Testing that everything is set up correctly*
To test whether your SSH key was added correctly, run the following command in your terminal 

ssh -T git@gitlab.aicrowd.com


Then you can create a submission by making a *tag push* to your repository, adding the correct git remote and pushing to the remote:

```
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit

# Add AICrowd git remote endpoint
git remote add aicrowd git@gitlab.aicrowd.com:<YOUR_AICROWD_USER_NAME>/food-recognition-challenge-starter-kit.git
git push aicrowd master

# Create a tag for your submission and push
git tag -am "submission-v0.1" submission-v0.1
git push aicrowd master
git push aicrowd submission-v0.1

# Note : If the contents of your repository (latest commit hash) does not change, 
# then pushing a new tag will not trigger a new evaluation.
```


You now should be able to see the details of your submission at : 
[gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/food-recognition-challenge-starter-kit/issues](gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/food-recognition-challenge-starter-kit/issues)


## Using http instead of ssh (Personal Access Token):

In order to use http to clone repositories and submit on gitlab:

a) Create a personal access token

1.  Log in to GitLab.
    
2.  In the upper-right corner, click your avatar and select Settings.
    
3.  On the User Settings menu, select Access Tokens.
    
4.  Choose a name and optional expiry date for the token.
    
5.  Choose the desired scopes.
    
6.  Click the Create personal access token button.
    
7.  Save the personal access token somewhere safe, lets call it XXX for now.
    

Once you leave or refresh the page, you won’t be able to access it again.

b) to clone a repo use the following command:

git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit

cd food-recognition-challenge-starter-kit


c)submit a solution:
```
cd into your submission repo on gitlab

cd (repo_name)

#Add AICrowd git remote endpoint

git remote add aicrowd https://oauth2:XXX@gitlab.aicrowd.com/(username)/(repo_name).git

git push aicrowd master

# Create a tag for your submission and push

git tag -am "submission-v0.1" submission-v0.1

git push aicrowd master

git push aicrowd submission-v0.1

# Note : If the contents of your repository (latest commit hash) does not change,

# then pushing a new tag will not trigger a new evaluation.
```

**Best of Luck**

## Miscelaneous Resources
* [Convert Annotations from MS COCO format to PascalVOC format](https://github.com/CasiaFan/Dataset_to_VOC_converter/blob/master/anno_coco2voc.py)

# ✍️ Author   
**[Sharada Mohanty](https://twitter.com/memohanty?lang=en)**

### ✨ Contributers

* [Nikhil Rayaprolu](https://github.com/nikhilrayaprolu)
* [Pulkit Gera](https://github.com/darthgera123)
* [Shivam Khandelwal](https://twitter.com/skbly7?lang=en)
