## Enable display forwarding
```bash
xhost +local:docker
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

## If you want to make sure the project is built correctly, run the script found in `/simulator/recompile.sh`
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
