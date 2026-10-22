import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    share = get_package_share_directory('autonav_bringup')
    gz_share = get_package_share_directory('ros_gz_sim')
    world = os.path.join(share, 'worlds', 'warehouse.sdf')
    model_path = os.path.join(share, 'models')
    resource_path = os.pathsep.join(filter(None, [model_path, os.environ.get('GZ_SIM_RESOURCE_PATH', '')]))

    bridge = Node(
        package='ros_gz_bridge', executable='parameter_bridge', output='screen',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/model/autonav_robot/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
        ],
        remappings=[('/model/autonav_robot/tf', '/tf')],
        parameters=[{'use_sim_time': True}],
    )
    lidar_tf = Node(
        package='tf2_ros', executable='static_transform_publisher',
        arguments=['--x', '0.10', '--y', '0', '--z', '0.13',
                   '--roll', '0', '--pitch', '0', '--yaw', '0',
                   '--frame-id', 'base_link', '--child-frame-id', 'lidar_link'],
        output='screen',
    )
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gz_share, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': f'-r {world}'}.items(),
    )
    return LaunchDescription([SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', resource_path), gazebo, bridge, lidar_tf])
