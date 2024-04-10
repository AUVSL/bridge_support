from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution, LaunchConfiguration
from launch_ros.descriptions import ComposableNode

def generate_launch_description():


    sensor_hostname = LaunchConfiguration('sensor_hostname', default='os-122318001257.local')
    timestamp_mode = LaunchConfiguration('timestamp_mode', default='TIME_FROM_ROS_TIME')
    viz = LaunchConfiguration('viz', default='false')

    # Include the ouster_ros sensor launch file
    # ouster_launch = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             PathJoinSubstitution([
    #                 FindPackageShare('launch_tutorial'),
    #                 'launch',
    #                 'example_substitutions.launch.py'
    #             ])
    #         ]),
    #         launch_arguments={
    #             'turtlesim_ns': 'turtlesim2',
    #             'use_provided_red': 'True',
    #             'new_background_r': TextSubstitution(text=str(colors['background_r']))
    #         }.items()
    #     )

    # quat = tf_transformations.quaternion_from_euler(
    #             float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]))
    static_transforms = ComposableNodeContainer(
        name='static_transforms',
        package='rclcpp_components',
        executable='component_container',
        namespace='',
        composable_node_descriptions=[
            ComposableNode(
                package='tf2_ros',
                plugin='tf2_ros::StaticTransformBroadcasterNode',
                name='static_tf_ousterlink_to_ossensor',
                parameters=[{
                    "frame_id": "ouster_lidar_link",
                    "child_frame_id": "os_sensor",
                    "translation.x": 0.0,
                    "translation.y": 0.0,
                    "translation.z": 0.0,

                    "rotation.x": 0.0,
                    "rotation.y": 0.0,
                    "rotation.z": 0.0,
                    "rotation.w": 1.0
                }]),
            ComposableNode(
                package='tf2_ros',
                plugin='tf2_ros::StaticTransformBroadcasterNode',
                name='static_tf_ousterlink_to_cameralink',
                parameters=[{
                    "frame_id": "ouster_lidar_link",
                    "child_frame_id": "camera_link",
                    "translation.x": 0.0,
                    "translation.y": 0.0,
                    "translation.z": -0.1,

                    "rotation.x": 0.0,
                    "rotation.y": 0.0,
                    "rotation.z": 0.0,
                    "rotation.w": 1.0
                }])
            ],
        output='screen'
    )

    return LaunchDescription([
        # Static TF Publishers
        static_transforms
        # staticTF_ouster_lidar_to_os_sensor,
        # staticTF_ouster_lidar_to_camera    
  ])