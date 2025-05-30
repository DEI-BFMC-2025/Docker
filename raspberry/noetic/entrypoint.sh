#!/bin/bash
# Source ROS and your catkin workspace setup
source /opt/ros/noetic/setup.bash

# Build the workspace if the devel folder doesn't exist 
if [ ! -d "/catkin_ws/devel" ]; then
  cd /catkin_ws && catkin_make
fi

source ~/catkin_ws/devel/setup.bash

# get rid of a warning
export LD_PRELOAD=/usr/local/lib/python3.8/dist-packages/sklearn/__check_build/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0

# Trigger udev events and settle them (detect devices plugged in after container start)
udevadm trigger
udevadm settle

# Execute the command passed to the container
exec "$@"
