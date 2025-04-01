## Enable display forwarding
```sh
xhost +local:docker
```

## Start the container
```sh
docker compose up -d
```

## Enter the container
```sh
docker compose exec gazebo_simulator bash
```

## If you want to make sure the project is built correctly, run the script found in `/simulator/recompile.sh`
```sh
./recompile.sh
```

## Source
```sh
source devel/setup.bash
```

## Launch the simulation
```sh
roslaunch sim_pkg map_2024.launch
```

## Source again (if needed)
```sh
source devel/setup.bash
```

## Run the brain script
```sh
cd brain/src/smart
python3 main_brain.py
