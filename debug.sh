#!/bin/bash



nvidia-docker run -it \
  --net=host \
  -v ${TEST_IMAGES_PATH}:/test_images \
  -v /tmp:/tmp_host \
  -e AICROWD_IS_GRADING=True \
  -e AICROWD_TEST_IMAGES_PATH="/test_images" \
  -e AICROWD_PREDICTIONS_OUTPUT_PATH="/tmp/output.json" \
  $IMAGE_NAME \
  /home/aicrowd/run.sh
