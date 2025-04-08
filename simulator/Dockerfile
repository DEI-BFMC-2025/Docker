FROM ghcr.io/sloretz/ros:noetic-simulators-osrf

# Update and install any necessary packages (x11-apps for testing)
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-tk \
    x11-apps \
    gdb \
    pcmanfm \
    featherpad \
    lxtask \
    xterm \
    && rm -rf /var/lib/apt/lists/*
    
COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# Set environment variables for X11 forwarding
ENV DISPLAY=:1
ENV QT_X11_NO_MITSHM=1

# Create workspace
WORKDIR /root/bfmc

# Expose ports if needed for ROS
EXPOSE 11311


# Source ROS setup file in the environment
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "ROS_MASTER_URI=http://localhost:11311" >> ~/.bashrc
RUN echo "ROS_HOSTNAME=localhost" >> ~/.bashrc
RUN echo "source /root/bfmc/simulator/devel/setup.bash" >> ~/.bashrc

# Use bash for the default shell
SHELL ["/bin/bash", "-c"]  
RUN source /opt/ros/noetic/setup.bash

# Default command to bash
#CMD ["bash"]
