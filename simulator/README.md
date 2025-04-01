## Enable display forwarding
```bash
xhost +local:docker
```

## Start the container
```bash
docker compose up -d
```

## Enter the container
```bash
docker compose exec gazebo_simulator bash
```

## If you want to make sure the project is built correctly, run the script found in `/simulator/recompile.sh`
```bash
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

## Source again
```bash
source devel/setup.babash
```

## Run the brain script
```bash
cd brain/src/smart
python3 main_brain.py
```
