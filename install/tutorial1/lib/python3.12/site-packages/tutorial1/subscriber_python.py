import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

topic1 = 'float_topic'
topic2 = 'string_topic'

class SubscriberNode(Node):
    """
    This class is a ROS2 node that subscribes to messages on two topics: one for float messages and one for string messages.
    It inherits from the Node class provided by rclpy.
    """

    def __init__(self):
        """
        Constructor for the SubscriberNode class. Initializes the node, creates subscribers, and sets up timers for processing messages.
        """
        super().__init__('subscriber_node')
        self.float_subscriber = self.create_subscription(Float32, topic1, self.callback_fun1, 10)

        self.string_subscriber = self.create_subscription(String, topic2, self.callback_fun2, 10)

        self.float_subscriber #to prevent unused variable warning
        self.string_subscriber
    

    def callback_fun1(self, msg):
        """
        Callback function for the float subscriber. This function is called every time a Float32 message is received on the specified topic.
        """
        self.get_logger().info('Received float message: "%f"' % msg.data)

    def callback_fun2(self, msg):
        """
        Callback function for the string subscriber. This function is called every time a String message is received on the specified topic.
        """
        self.get_logger().info('Received string message: "%s"' % msg.data)

def main(args=None):
    """
    Main function to initialize the ROS2 node and start the subscription process.
    """
    rclpy.init(args=args)

    subscriber_node = SubscriberNode()

    rclpy.spin(subscriber_node)

    subscriber_node.destroy_node()
    rclpy.shutdown()

    #creating an entry point for the script to be run as a standalone program
    if __name__ == '__main__':
        main()