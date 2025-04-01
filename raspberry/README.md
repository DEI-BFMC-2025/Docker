## Before starting the container
In the docker-compose file you need to edit the shared directory containing the ros project. The shared folders are writen like this in the file ```folder/path/on/host:folder/path/on/container```, you need to change the one pointing to ```/catkin_ws/src```; for example if you have the ros project called "Brain" on the Desktop you can use ```/home/${USER}/Desktop/Brain:/catkin_ws/src```. The directory gets shared/linked from host to the docker continers. This way any changes done from inside the container are gonna be seen on the host and vice versa. The advantage is that you can use VsCode on the host to code more easily.

## Start the Containers

Run ```docker compose up -d``` inside this folder, if is done for the first time is gonna download the docker image and build it, and then build the container. The compose package/library uses the docker-compose.yml file found in the current directory.

Run ```docker compose exec picamera bash``` to enter the picamera container. Here we start the picamera client, found in ```/app/client.py```. The client names comes from the fact that he is the one that waits for a server to start the comunication by creating a unix.socket

Run ```docker compose exec ros bash``` the brain project is in the folder ```/catkin_ws/src```. Before running the project if not already done build it by running ```catkin_make``` inside the catkin_ws folder nowhere other. Source by using ```source devel/setup.bash```. Launch the ros nodes ```roslaunch utils run_automobile_2025```. Then you are free to start the main_brain.
