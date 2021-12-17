# <center>Food Recognition Benchmark - Starter Kit</center>

![Food-Challenge](https://i.imgur.com/haaT8Cu_d.webp?maxwidth=1520&fidelity=grand)

<p align="center"><a href="https://discord.gg/GTckBMx"><img src="https://img.shields.io/discord/657211973435392011?style=for-the-badge" alt="chat on Discord"></a></p>


<p align="center">This repository is the main Food Recognition Benchmark template and Starter kit!</p>
<p align="center">Clone the repository to compete now!</p>
<p align="center">
<a href="https://www.aicrowd.com/challenges/food-recognition-benchmark-2022">👉 Benchmark Website</a></p>

----

# 🏆 About the Benchmark

<img src="https://i.imgur.com/YvIIgOZ.png">

This data set has been annotated - or automatic annotations have been verified - with respect to segmentation, classification (mapping the individual food items onto an ontology of Swiss Food items), and weight/volume estimation.

The goal of this benchmark is to train models which can look at images of food items and detect the individual food items present in them. 

![](https://i.imgur.com/xzQkwKV.jpg)

# Table of contents

<details align="left">
<summary>💪 Getting Started</summary>

* [Using this repository](#using-this-repository)
* [Using colab starter kit](#using-colab-starter-kit)
* [Running the code locally](#running-the-code-locally)
</details>


<details align="left">
<summary>👥 Participation</summary>

* [Quick Participation 🏃](#-participation)
* [Active Participation 👨‍💻](#-participation)
</details>


<details align="left">
<summary>🧩 Repository Structure</summary>

* [Required files](#required-files)
* [Other files](#other-files)
</details>

<details align="left">
<summary>🚀 Submission</summary>


* [Quick Participation 🏃](#-submission)
* [Active Participation 👨‍💻](#-submission)
</details>

<br>

# 💪 Getting Started

## Download Dataset

[![](https://i.imgur.com/EnD7Rvl.png)](https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/dataset_files)


## Using this repository

This repository contains prediction codebase for `mmdetection`, `detectron2` and random agents.

```bash
# Clone the repository
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit

# Install dependencies
pip install -r requirements.txt

# Download the dataset, and place it in `data/images/`

# Run model locally
./run.sh
```

This will generate `predictions.json` file in your current directory.

# 👥 Participation

Before we do a deep dive into submissions. Check which user persona suits you the best!

<table style="undefined;table-layout: fixed; width: 602px">
<colgroup>
<col style="width: 301px">
<col style="width: 301px">
</colgroup>
<thead>
  <tr>
    <th>Quick Participation 🏃</th>
    <th>Active Participation 👨‍💻</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>You need to upload json prediction files</td>
    <td>You need to submit code (and AIcrowd evaluators runs the code to generate predictions)</td>
  </tr>
  <tr>
    <td>Scores are computed on 40% of the publicly released test set </td>
    <td>Scores are computed on 100% of the publicly released test set + 40% of the (unreleased) extended test set</td>
  </tr>
  <tr>
    <td>You are not eligible for the final leaderboard (and prizes)</td>
    <td>You are eligible for the final leaderboard and prizes</td>
  </tr>
</tbody>
</table>

# 🧩 Repository structure

## Required files

**File** | **Description**
--- | ---
`aicrowd.json` | A configuration file used to identify the challenge and resources needed for evaluation
`apt.txt` | List of packages that should be installed (via `apt`) for your code to run
`requirements.txt` | List of python packages that should be installed (via `pip`) for your code to run
`predict.py` | Entry point to your model


## Other important files

**File** | **Description**
--- | ---
`score.py` | Helps your generate score for your run locally
`utils/` | Directory containing some useful scripts and notebooks
`utils/requirements_detectron2.txt` | A sample `requirements.txt` file for using `detectron2`
`utils/requirements_mmdetection.txt` | A sample `requirements.txt` file for using `mmdetection`

# 🚀 Submission


## Quick Participation 🏃

As promised, we will keep it quick for you. Participating is as simple as:

- Generate your predictions using the starter kit
- Upload them on the [benchmark website](https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/submissions/new)
- Get scores, iterate, improve! 💪

## Active Participation 👨‍💻

- Prepare your runtime environment
- Setup SSH keys for your AIcrowd repository
- Make submissions by simple git tag pushes
- Get scores, **more scores** 😉, iterate faster, improve faster! 💪

More details for active participation in present in [SUBMISSION.md](/utils/SUBMISSION.md)

# 📎 Important links


- 💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/food-recognition-benchmark-2022
- 🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/discussion
- 🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/leaderboards
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
  
# ✍️ Maintainers
* **[Sharada Mohanty](https://twitter.com/memohanty?lang=en)**
* **[Shivam Khandelwal](https://twitter.com/skbly7?lang=en)**

## Thanks to our awesome contributors! ✨ 
<br>
<a href="https://github.com/AIcrowd/food-recognition-challenge-starter-kit/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AIcrowd/food-recognition-challenge-starter-kit" />
</a>
