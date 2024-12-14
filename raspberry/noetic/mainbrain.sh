#!/bin/bash

source /opt/ros/noetic/setup.bash

cd /catkin_ws/ && catkin_make

source devel/setup.bash

export LD_PRELOAD=/usr/local/lib/python3.8/dist-packages/sklearn/__check_build/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0

cd src/ws_2024/src/smart/ && python3 main_brain.py



