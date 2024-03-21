import rclpy
from rclpy.node import Node
from grid_map_msgs import GridMap

class ElevMapModifier(Node):
    def __init__(self):
        super().__init__('elev_map_modifier node')
        self.pub = self.create_subscription(GridMap, "/elevation_mapping/elevation_map_raw", self.elevation_map_cb, 10)

    def lookup_transform(self, target_frame, source_frame):
        try:
            now = rclpy.time.Time()
            return self.tf_buffer.lookup_transform(target_frame, source_frame, now)
            # self.get_logger().info(f'Transform: {transform}')
        except Exception as e:
            self.get_logger().info(f'Could not transform {target_frame} to {source_frame}: {e}')
            return None

    def elevation_map_cb(self, data):
        modified_msg = GridMap()

        

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