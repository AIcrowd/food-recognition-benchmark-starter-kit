FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential \
    bzip2 \
    cmake \
    curl \
    git \
    g++ \
    libboost-all-dev \
    pkg-config \
    rsync \
    software-properties-common \
    sudo \
    tar \
    timidity \
    unzip \
    wget \
    locales \
    zlib1g-dev \
    python3-dev \
    python3 \
    python3-pip \
    python3-tk \
    libjpeg-dev \
    libpng-dev

# Python3
RUN pip3 install pip --upgrade
RUN pip3 install cython aicrowd_api timeout_decorator \
  numpy \
  matplotlib \
  aicrowd-repo2docker \
  pillow
RUN pip3 install git+https://github.com/AIcrowd/coco.git#subdirectory=PythonAPI
RUN pip3 install tensorflow-gpu

# Unicode support:
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Enables X11 sharing and creates user home directory
ENV USER_NAME aicrowd
ENV HOME_DIR /home/$USER_NAME
#
# Replace HOST_UID/HOST_GUID with your user / group id (needed for X11)
ENV HOST_UID 1000
ENV HOST_GID 1000

RUN export uid=${HOST_UID} gid=${HOST_GID} && \
    mkdir -p ${HOME_DIR} && \
    echo "$USER_NAME:x:${uid}:${gid}:$USER_NAME,,,:$HOME_DIR:/bin/bash" >> /etc/passwd && \
    echo "$USER_NAME:x:${uid}:" >> /etc/group && \
    echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER_NAME && \
    chmod 0440 /etc/sudoers.d/$USER_NAME && \
    chown ${uid}:${gid} -R ${HOME_DIR}

USER ${USER_NAME}
WORKDIR ${HOME_DIR}

COPY . .

RUN sudo chown ${HOST_UID}:${HOST_GID} -R *
RUN sudo chmod 775 -R *
