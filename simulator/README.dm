**Reset docker if it can't download/isntall packages whe building the image or inside the container** 
sudo systemctl restart docker
**Remove the <none> iamges**
docker rmi $(docker images -f "dangling=true" -q)
**Enable display forwarding**
xhost +local:docker

docker-compose up --build
docker exec -it gazebo_simulator bash

source /opt/ros/noetic/setup.bash
source src/simulator_2024/simulator_2024/devel/setup.bash

roslaunch sim_pkg map_2024.launch 

catkin_make --pkg utils
catkin_make

export GAZEBO_MODEL_PATH="/root/catkin_ws/src/simulator_2024/simulator_2024/src/models_pkg:$GAZEBO_MODEL_PATH"
export ROS_PACKAGE_PATH="/root/catkin_ws/src/simulator_2024/simulator_2024/src:$ROS_PACKAGE_PATH"

export GAZEBO_MODEL_PATH="/home/eugen/catkin_ws/src/simulator_2024/simulator_2024/src/models_pkg:$GAZEBO_MODEL_PATH"
export ROS_PACKAGE_PATH="/home/eugen/catkin_ws/src/simulator_2024/simulator_2024/src:$ROS_PACKAGE_PATH"
