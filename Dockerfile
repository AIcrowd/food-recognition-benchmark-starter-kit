FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive

# Install needed apt packages
COPY apt.txt apt.txt
RUN apt -qq update && xargs -a apt.txt apt -qq install -y --no-install-recommends \
 && rm -rf /var/cache/*

# Create user home directory
ENV USER aicrowd
ENV HOME_DIR /home/$USER

# Replace HOST_UID/HOST_GUID with your user / group id
ENV HOST_UID 1001
ENV HOST_GID 1001

# Use bash as default shell, rather than sh
ENV SHELL /bin/bash

# Set up user
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${HOST_UID} \
    ${USER}
USER ${USER}
WORKDIR ${HOME_DIR}
ENV CONDA_DIR ${HOME_DIR}/.conda
ENV PATH ${CONDA_DIR}/bin:${PATH}

# Download miniconda for python
RUN wget -nv -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh \
 && bash miniconda.sh -b -p ${CONDA_DIR} \
 && . ${CONDA_DIR}/etc/profile.d/conda.sh \
 && rm -rf miniconda.sh \
 && conda clean -a -y

# Install needed pypi packages
USER ${USER}
RUN pip install numpy cython --no-cache-dir
COPY --chown=1001:1001 requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy user files
COPY --chown=1001:1001 . ${HOME_DIR}
