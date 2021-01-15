# <center>Food Recognition Challenge - Starter Kit</center>

![Food-Challenge](https://i.imgur.com/0G3PEc7.png)

<p align="center">
 <a href="https://discord.gg/GTckBMx"><img src="https://img.shields.io/discord/657211973435392011?style=for-the-badge" alt="chat on Discord"></a>
</p>

# Table of contents
- [💪 Getting Started](#-getting-started)
  * [Using this repository](#using-this-repository)
  * [Using colab starter kit](#using-colab-starter-kit)
  * [Running the code locally](#running-the-code-locally)
- [🧩 Repository structure](#-repository-structure)
  * [Required files](#required-files)
  * [Other files](#other-files)
- [🚀 Submission](#-submission)
  * [Prepare your environment](#prepare-your-environment)
    + [`Dockerfile`](#dockerfile)
    + [`apt.txt`](#apttxt)
    + [`requirements.txt`](#requirementstxt)
  * [Initial setup](#initial-setup)
  * [Submit to AIcrowd](#submit-to-aicrowd)
- [🛠 Troubleshooting](#-troubleshooting)
  * [My submission failed. How do I know what happened?](#my-submission-failed-how-do-i-know-what-happened)
  * [My docker builds fail. Can I reproduce this locally?](#my-docker-builds-fail-can-i-reproduce-this-locally)
- [📎 Important links](#-important-links)
- [✍️ Author](#-author)
  * [✨ Contributors](#-contributors)



# 💪 Getting Started

The dataset for this challenge is available on the [challenge's resources page](https://www.aicrowd.com/challenges/food-recognition-challenge/dataset_files).

## Using this repository
This repository contains the code for a random agent. To run the code locally,

- Clone the repository
- Install dependencies
- Execute `run.sh`

Clone the repository
```bash
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit
```

Install dependencies
```bash
pip install -r requirements.txt
```

Update the value for `AICROWD_TEST_IMAGES_PATH` to point to your validation dataset
and run `debug.sh`
```bash
./debug.sh
```

During the evaluation, we will execute `run.sh`. You can add any additional commands
as per your needs.

## Using colab starter kit

We prepared a colab notebook that uses `detectron2`. You can train your agent and make
a submission from your notebook!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1F2IbqpI0ecbRDCNiBLPFCCOVEK0cgbH7?usp=sharing)

## Running the code locally

- First, make sure that you have the dataset downloaded.
- Update the value of `AICROWD_TEST_IMAGES_PATH` in `debug.sh` file to point to your dataset
- Execute `debug.sh`

```bash
./debug.sh
```

This will generate `predictions.json` file in your current directory.

# 🧩 Repository structure

## Required files

**File** | **Description**
--- | ---
`Dockerfile` | Configuration file to build docker images used during evaluation
`aicrowd.json` | A configuration file used to identify the challenge and resources needed for evaluation
`aicrowd_helpers.py`<sup>#</sup> | Helpers file used to relay evaluation progress
`apt.txt` | List of packages that should be installed (via `apt`) for your code to run
`requirements.txt` | List of python packages that should be installed (via `pip`) for your code to run
`run.sh` | Entry point to your code

<sup>#</sup> Do not edit these files.

## Other files

**File** | **Description**
--- | ---
`run.py` | Python script to generate random predictions
`debug.sh` | Helps your run your code locally
`utils/` | Directory containing some useful scripts and notebooks
`utils/requirements_detectron2.txt` | A sample `requirements.txt` file for using `detectron2`
`utils/requirements_mmdetection.txt` | A sample `requirements.txt` file for using `mmdetection`


# 🚀 Submission

## Prepare your environment

There are three files that help you setup your environment.
1. `Dockerfile`
2. `apt.txt`
3. `requirements.txt`

### `Dockerfile`
If you plan to use GPU, please make sure that you are using an appropriate `CUDA` and
`CUDNN` versions. You can specify these at the top of your [`Docerfile`](Dockerfile#L1).

### `apt.txt`
If there are certain system level packages that you need, you can specify them in your
`apt.txt`. If you are familiar with ubuntu/debian, this is same as installing these
packages using `apt-get install` command.

### `requirements.txt`
You can specify the list of python packages that need to be installed in your
`requirements.txt`.

Please note that we are using `apt.txt` and `requirements.txt` in the `Dockerfile` to
install required packages. We believe that this makes it easier for you to add the
required packages without much hassle. If you are comfortable with docker, you are
free to edit the `Dockerfile` as needed.

## Initial setup

Before you submit to AIcrowd, you need to setup SSH access to our GitLab instance.
This is a one-time requirement to setup your repository.

This process involves
1. Cloning the repository
2. Replace git origin to point to your personal repository
3. Setup SSH key

To clone the repository, please refer getting started section.

Now, you need to point the repository to your personal repository on AIcrowd GitLab.

```bash
git remote set-url origin git@gitlab.aicrowd.com:<your-aicrowd-username>/food-recognition-challenge-starter-kit.git
```

To be able to push your code to GitLab, you should setup SSH keys first. Please
follow the instructions at
[https://discourse.aicrowd.com/t/how-to-add-ssh-key-to-gitlab/2603](https://discourse.aicrowd.com/t/how-to-add-ssh-key-to-gitlab/2603)

## Submit to AIcrowd

To submit to AIcrowd, you need to push a tag starting with `submission-` to GitLab.

Add the changes to git.

```bash
git add --all
git commit -m "<brief summary of changes>"
```

You need to add large files via `git-lfs`.

```bash
git lfs install

# Add all the files larger than 5 MB to LFS
find . -type f -size +5M -exec git lfs migrate import --include={} &> /dev/null \;
```

For more information on using LFS, please refer
[uploading large files to GitLab](https://discourse.aicrowd.com/t/how-to-upload-large-files-size-to-your-submission/2304).

Create and push the tag

```bash
# You can replace "-initial-version" with something that describes your submission
git tag -am "submission-initial-version" "submission-initial-version"
git lfs push origin master
git push origin master
git push origin submission-initial-version
```

# 🛠 Troubleshooting

## My submission failed. How do I know what happened?

If you make a submission in `debug` mode, we provide the outputs from your code on the
GitLab issue page corresponding to your submission. To make a submission in `debug`
mode, you need to add `"debug": true` in your `aicrowd.json`. Please note that the
debug mode submission will not be considered for leaderboard.

## My docker builds fail. Can I reproduce this locally?

You can build the images locally by running the following

```bash
docker build .
```

# 📎 Important links


- 💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/food-recognition-challenge
- 🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/food-recognition-challenge/discussion
- 🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/food-recognition-challenge/leaderboards
- Resources - Round 1
  * [Colab Notebook for Data Analysis and Tutorial](https://colab.research.google.com/drive/1A5p9GX5X3n6OMtLjfhnH6Oeq13tWNtFO#scrollTo=ok54AWT_VoWV)
  * [Baseline with `mmdetection` (pytorch)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-pytorch-baseline)
  * [Baseline with `matterport-maskrcnn` (keras - tensorflow)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-recognition)
- Resources - Round 2
  * [Colab Notebook for Data Analysis and Tutorial](https://colab.research.google.com/drive/1vXdv9quZ7CXO5lLCjhyz3jtejRzDq221)
  * [Baseline with `mmdetection` (pytorch)](https://gitlab.aicrowd.com/nikhil_rayaprolu/food-round2)
- Resources - Round 3
  * [Colab Notebook for data exploration](https://discourse.aicrowd.com/t/detectron2-colab-notebook-from-data-exploration-to-training-the-model/3691)
- [Participant contributions](https://discourse.aicrowd.com/tags/c/food-recognition-challenge/112/explainer)
- External resources:
  * [Convert Annotations from MS COCO format to PascalVOC format](https://github.com/CasiaFan/Dataset_to_VOC_converter/blob/master/anno_coco2voc.py)
  

# ✍️ Author   
**[Sharada Mohanty](https://twitter.com/memohanty?lang=en)**

## ✨ Contributors

* [Nikhil Rayaprolu](https://github.com/nikhilrayaprolu)
* [Pulkit Gera](https://github.com/darthgera123)
* [Shivam Khandelwal](https://twitter.com/skbly7?lang=en)
* [Jyotish P](https://github.com/jyotishp)