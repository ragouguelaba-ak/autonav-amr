# Phase 1 acceptance
1. Gazebo warehouse opens and robot is visible.
2. /clock, /odom, /scan and /tf have live messages.
3. /cmd_vel forward motion moves robot and /odom position changes.
4. A zero Twist stops the robot.
5. XML asset tests pass.
6. Record a 30-second video and note failures in GitHub issues.

# Phase 2 prerequisites
Validate TF frame conventions and add robot_state_publisher, complete static sensor transforms, SLAM and Nav2. Phase 1 intentionally does not claim a complete navigation-ready TF tree.
