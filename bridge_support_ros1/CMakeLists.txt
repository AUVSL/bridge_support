cmake_minimum_required(VERSION 3.0.2)
project(bridge_support_ros1)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  custom_msgs_ros1
  roslaunch
  geometry_msgs
  rospy
  std_msgs
  tf2_ros
)

roslaunch_add_file_check(launch)

# catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
  src/GridMapTransformer.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  launch/bringup_all.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
