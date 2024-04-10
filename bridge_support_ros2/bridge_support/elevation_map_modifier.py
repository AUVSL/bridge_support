import rclpy
from rclpy.node import Node
from grid_map_msgs.msg import GridMap, GridMapInfo
from std_msgs.msg import Header
from custom_msgs.msg import PseudoGridMap
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

class ElevMapModifier(Node):
    def __init__(self):
        super().__init__('elev_map_modifier_node')
        qos_profile = QoSProfile(
            reliability = ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.sub = self.create_subscription(PseudoGridMap, "/bridge/elevation_map_raw", self.elevation_map_cb, qos_profile=qos_profile)
        self.pub = self.create_publisher(GridMap, "/elevation_mapping/elevation_map_raw", 10)
        
    def elevation_map_cb(self, data):
        new_grid_map = GridMap()

        new_header = Header()
        new_header.stamp = rclpy.time.Time().to_msg()
        new_header.frame_id = data.header.frame_id

        new_grid_map.header = data.header

        # instantiate grid map info and fill it's fields        
        new_grid_map_info = GridMapInfo()
        new_grid_map_info.resolution = data.resolution
        new_grid_map_info.length_x = data.length_x
        new_grid_map_info.length_y = data.length_y
        new_grid_map_info.pose = data.pose

        new_grid_map.info = new_grid_map_info

        new_grid_map.layers = data.layers
        new_grid_map.basic_layers = data.basic_layers
        new_grid_map.data = data.data
        new_grid_map.outer_start_index = data.outer_start_index
        new_grid_map.inner_start_index = data.inner_start_index

        self.pub.publish(new_grid_map)


def main(args=None):
    rclpy.init(args=args)
    try:
        node = ElevMapModifier()
        rclpy.spin(node)
    except rclpy.exceptions.ROSInterruptException:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()