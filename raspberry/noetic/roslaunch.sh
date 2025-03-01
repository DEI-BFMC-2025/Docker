#!/bin/bash

source /opt/ros/noetic/setup.bash

#cd /catkin_ws/ && catkin_make

source /catkin_ws/devel/setup.bash

export LD_PRELOAD=/usr/local/lib/python3.8/dist-packages/sklearn/__check_build/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0

roslaunch utils run_automobile_2024

#cd /src/smart/ && python3 main_brain.py



