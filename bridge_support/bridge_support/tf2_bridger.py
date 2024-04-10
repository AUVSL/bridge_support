import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
from tf2_msgs.msg import TFMessage

class TF2ListenerNode(Node):
    def __init__(self):
        super().__init__('tf2_listener_node')
        self.tf_buffer = Buffer()
        self.create_timer(0.1, self.timer_callback)
        self.listener = TransformListener(self.tf_buffer, self)
        self.pub = self.create_publisher(TFMessage, "test/tf", 10)

    def lookup_transform(self, target_frame, source_frame):
        try:
            now = rclpy.time.Time()
            return self.tf_buffer.lookup_transform(target_frame, source_frame, now)
            # self.get_logger().info(f'Transform: {transform}')
        except Exception as e:
            self.get_logger().info(f'Could not transform {target_frame} to {source_frame}: {e}')
            return None

    def timer_callback(self):

        transform_odom = self.lookup_transform('odom', 'base_footprint')
        # transform_lidar = self.lookup_transform("base_footprint", "os_lidar")
        # transform_camera = self.lookup_transform("base_footprint", "camera_color_optical_frame")

        transforms = [transform_odom]

        if not any(transform is None for transform in transforms):
            tf_msg = TFMessage(transforms = transforms)
            # self.get_logger().info(f'Transforms Published: {transforms}')
            self.get_logger().info("Publishing TF")
            self.pub.publish(tf_msg)

def main(args=None):
    rclpy.init(args=args)
    try:
        node = TF2ListenerNode()
        rclpy.spin(node)
    except rclpy.exceptions.ROSInterruptException:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()