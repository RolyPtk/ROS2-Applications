
# rclpy is the ros2 library for python. It is used to create nodes, publishers, subscribers, and other ROS2 entities in Python.

import rclpy

# import Node class from rclpy.node module. The Node class is the base class for all ROS2 nodes in Python.
from rclpy.node import Node

#import the types of messages being sent in this application. In this case, we are sending String and Float32 messages.
from std_msgs.msg import String
from std_msgs.msg import Float32

#topic for the float message
topic1 = 'float_topic'

#topic for the string message
topic2 = 'string_topic'

#here we define a class called PublisherNode that inherits from the Node class. This class will be responsible for 
#publishing messages to the specified topics.
#The parent class is the standard ROS2 Node class, which provides the basic functionality for creating a node in ROS2. 
#By inheriting from this class, PublisherNode can utilize all the features and methods provided by the Node class, 
# such as creating publishers, subscribers, timers, and logging.
class PublisherNode(Node):
    """
    This class is a ROS2 node that publishes messages to two topics: one for float messages and one for string messages.
    It inherits from the Node class provided by rclpy.
    """

    #default constructor of the Node
    def __init__(self):
        """
        Constructor for the PublisherNode class. Initializes the node, creates publishers, and sets up timers for publishing messages.
        """
        # Initialize the node with the name 'publisher_node'
        super().__init__('publisher_node')

        # Create a publisher for Float32 messages on the specified topic with a queue size of 10
        self.float_publisher = self.create_publisher(Float32, topic1, 10)

        # Create a publisher for String messages on the specified topic with a queue size of 10
        self.string_publisher = self.create_publisher(String, topic2, 10)

        # Create a timer that calls the callback function every 1 second   
        self.period = 1
        self.timer = self.create_timer(self.period, self.callback_fun)

        #message counter
        self.counter = 0
        #float value
        self.value = 0


    def callback_fun(self):
        """
        Callback function for the timer. This function is called every time the timer expires.
        """
        message1 = Float32()
        message2 = String()

        self.value = self.value + 0.01
        message1.data = self.value
        message2.data = 'Message number: %d' % self.counter

        # Publish the messages to their respective topics
        self.string_publisher.publish(message2)
        self.float_publisher.publish(message1)

        self.get_logger().info('Publishing: "%s" and value "%f"' % (message2.data, message1.data))
        self.counter += 1

def main(args=None):
    """
    Main function to initialize the ROS2 node and start the publishing process.
    """
    # Initialize the ROS2 Python client library
    rclpy.init(args=args)

    # Create an instance of the PublisherNode
    publisher_node = PublisherNode()

    # Spin the node to keep it running and processing callbacks
    rclpy.spin(publisher_node)

    # Destroy the node explicitly (optional)
    publisher_node.destroy_node()

    # Shutdown the ROS2 client library
    rclpy.shutdown()