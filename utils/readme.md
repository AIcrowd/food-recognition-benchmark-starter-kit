# Building image for `detectron2`

To build an image for detectron2, simply copy and paste the
`requirements_detectron2.txt` file to `requirements.txt` in the root of the
repository.

# Building image for `mmdetection`

The easiest way to install `mmdetection` is to use the pytorch docker image and
use the `requirements_mmdetection.txt` provided in this directory.

Make the following changes to the Dockerfile

```diff
- RUN wget -nv -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh \
-  && bash miniconda.sh -b -p ${CONDA_DIR} \
-  && . ${CONDA_DIR}/etc/profile.d/conda.sh \
-  && rm -rf miniconda.sh \
-  && conda clean -a -y

+ RUN wget -nv -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh \
+  && bash miniconda.sh -b -p ${CONDA_DIR} \
+  && . ${CONDA_DIR}/etc/profile.d/conda.sh \
+  && rm -rf miniconda.sh \
+  && conda install pytorch==1.5.1 torchvision==0.6.1 cudatoolkit=10.1 -c pytorch \
+  && conda clean -a -y
+ ENV FORCE_CUDA="1"
```

You can replace
- `1.5.1` with any pytorch version that you want to use
- `10.1` with corresponding CUDA version for pytorch

Then, copy-paste `requirements_mmdetection.txt` file to `requirements.txt` in the
the root of the repository.
