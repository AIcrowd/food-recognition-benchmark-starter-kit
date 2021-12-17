# Active Participation - User Guide

## Prepare your runtime environment

There are three files that help you setup your environment.
1. `Dockerfile`
2. `apt.txt`
3. `requirements.txt`

#### `Dockerfile`
If you plan to use GPU, please make sure that you are using an appropriate `CUDA` and
`CUDNN` versions. You can specify these at the top of your [`Docerfile`](Dockerfile#L1).

#### `apt.txt`
If there are certain system level packages that you need, you can specify them in your
`apt.txt`. If you are familiar with ubuntu/debian, this is same as installing these
packages using `apt-get install` command.

#### `requirements.txt`
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

Clone the repository using:
```bash
git clone https://github.com/AIcrowd/food-recognition-challenge-starter-kit
cd food-recognition-challenge-starter-kit
```

Now, you need to point the repository to your personal repository on AIcrowd GitLab.

```bash
git remote set-url origin git@gitlab.aicrowd.com:<your-aicrowd-username>/food-recognition-challenge-starter-kit.git
```

To be able to push your code to GitLab, you should setup SSH keys first. Please
follow the instructions [here](https://discourse.aicrowd.com/t/how-to-add-ssh-key-to-gitlab/2603).

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

## Monitor progress and score

After you have done the submission, the progress and live scores will be visible on your GitLab repository -> Issues.

Example scores:

![](https://i.imgur.com/zCj7GZr.png)

The challenge uses the scores marked with ⭐ for the leaderboards.

<br><br>

# 🛠 Troubleshooting

### Q. My submission failed. How do I know what happened?

If you make a submission in `debug` mode, we provide the outputs from your code on the GitLab issue page corresponding to your submission. To make a submission in `debug` mode, you need to add `"debug": true` in your `aicrowd.json`. Please note that the debug mode submission will not be considered for leaderboard.

### Q. My docker builds fail. Can I reproduce this locally?

You can build the images locally by running the following

```bash
pip install -U aicrowd-repo2docker
aicrowd-repo2docker .
```

### Q. What is the code entrypoint?

The evaluator will execute `predict.py` for generating predictions, so please remember to edit it in your submission!

### Q. More questions?

In case you have any doubts or need help, you can reach out to us via [Challenge Discussions](https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/discussion) or [Discord](https://discord.gg/GTckBMx).