
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RobotController(Node):

    def __init__(self):
        super().__init__("robot_controller")

        self.publisher = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.start_time = self.get_clock().now()
        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.finished = False

    def control_loop(self):
        if self.finished:
            return

        elapsed = (
            self.get_clock().now() -
            self.start_time
        ).nanoseconds / 1e9

        command = Twist()

        if elapsed < 3.0:
            command.linear.x = 0.2

        elif elapsed < 6.0:
            command.angular.z = 0.5

        else:
            self.finished = True
            self.publisher.publish(Twist())
            self.get_logger().info(
                "Motion sequence completed"
            )
            rclpy.shutdown()
            return

        self.publisher.publish(command)


def main():
    rclpy.init()
    node = RobotController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.publisher.publish(Twist())
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
