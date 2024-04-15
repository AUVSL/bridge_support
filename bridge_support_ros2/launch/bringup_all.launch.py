from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource, FrontendLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution, LaunchConfiguration
from launch_ros.descriptions import ComposableNode

def generate_launch_description():


    sensor_hostname = "os-122318001257.local"
    timestamp_mode = "TIME_FROM_ROS_TIME"
    viz = "false"


    # Include the ouster_ros sensor launch file
    # ouster_launch = IncludeLaunchDescription(
    #         FrontendLaunchDescriptionSource([
    #             PathJoinSubstitution([
    #                 FindPackageShare('ouster_ros'),
    #                 'launch',
    #                 'sensor.launch.xml'
    #             ])
    #         ]),
    #         launch_arguments={
    #             'sensor_hostname': sensor_hostname,
    #             'timestamp_mode': timestamp_mode,
    #             'viz': viz
    #         }.items()
    #     )

    tf2_bridger = Node(
        package='bridge_support',
        namespace='',
        executable='tf2_bridger',
        name='tf2_bridger'
    )

    elevation_map_modifier = Node(
        package='bridge_support',
        namespace='',
        executable='elevation_map_modifier',
        name='elevation_map_modifier'
    )

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
        # ouster_launch,
        tf2_bridger,
        elevation_map_modifier,
        static_transforms
  ])