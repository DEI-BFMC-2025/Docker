## Enable display forwarding
```bash
xhost +local:docker
```

## Modify the docker-compose.yml file
```bash
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - /home/${USER}/Desktop/Brain:/root/bfmc  #adjust the directory containing the project
```

## Start the container
```bash
cd Docker/simulator
docker compose up -d
```

## Enter the container
```bash
docker compose exec gazebo_simulator bash
```

## Inside the container terminal, if you want to make sure the project is built correctly, run the script `/simulator/recompile.sh`
```bash
cd simulator
./recompile.sh
```

## Source
```bash
source devel/setup.bash
```

## Launch the simulation
```bash
roslaunch sim_pkg map_2024.launch
```

## Now in another tab, in order to run the brain, source again
```bash
source devel/setup.bash
```

## Run the brain script
```bash
cd brain/src/smart
python3 main_brain.py
```
