#!/usr/bin/env python
import rospy

from custom_msgs_ros1.msg import PseudoGridMap
from grid_map_msgs.msg import GridMap
from std_msgs.msg import String


def gridmap_callback(msg):
    pseudo_gridmap = PseudoGridMap()
    pseudo_gridmap.header = msg.info.header
    pseudo_gridmap.resolution = msg.info.resolution
    pseudo_gridmap.length_x = msg.info.length_x
    pseudo_gridmap.length_y = msg.info.length_y
    pseudo_gridmap.pose = msg.info.pose
    pseudo_gridmap.layers = msg.layers
    pseudo_gridmap.basic_layers = msg.basic_layers
    pseudo_gridmap.data = msg.data
    pseudo_gridmap.outer_start_index = msg.outer_start_index
    pseudo_gridmap.inner_start_index = msg.inner_start_index

    pub.publish(pseudo_gridmap)

    

rospy.init_node('GridMapTransformer')
sub = rospy.Subscriber("/elevation_mapping/elevation_map_raw", GridMap, gridmap_callback)
pub = rospy.Publisher("/bridge/elevation_map_raw", PseudoGridMap, queue_size=10)

rospy.spin()


