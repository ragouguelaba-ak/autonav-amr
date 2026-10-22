# AutoNav-AMR — Phase 1

ROS 2 Jazzy + Gazebo Harmonic differential-drive AMR simulation.

## Dependencies (Ubuntu 24.04)
```bash
sudo apt update
sudo apt install -y ros-jazzy-ros-gz ros-jazzy-tf2-ros python3-colcon-common-extensions python3-pytest
```

## Build
```bash
cd ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch autonav_bringup sim.launch.py
```

## Verify (new terminal)
```bash
source /opt/ros/jazzy/setup.bash
ros2 topic list
ros2 topic echo /scan --once
ros2 topic echo /odom --once
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.2}, angular: {z: 0.0}}'
```

Stop the velocity publisher with Ctrl+C and send a zero velocity command.

## Test
```bash
cd ros2_ws
colcon test --packages-select autonav_bringup
colcon test-result --verbose
```

## Notes
- Simulation only. No watchdog, collision monitor or hardware safety controller yet.
- `odom -> base_link` TF is bridged from Gazebo, and `base_link -> lidar_link` is static.
- This starter has not been executed against a ROS/Gazebo installation in the generation environment.
