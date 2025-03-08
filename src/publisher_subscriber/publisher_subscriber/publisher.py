from std_msgs.msg import String

import rclpy

from rclpy.node import Node

topicName = 'communication_topic'


class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publishersCreated = self.create_publisher(String, topicName, 20)
        self.counter = 0
        communicationPeriod = 1
        self.period = self.create_timer(communicationPeriod, self.callBackFunctionPublisher)

    def callBackFunctionPublisher(self):
        # we create an empty Message data structure
        messageToBeSent = String()
        # we are sending this string
        messagePythonString = 'This is message number %d' % self.counter
        # fill-in the data to be sent
        messageToBeSent.data = messagePythonString

        # send the message through the topic
        self.publishersCreated.publish(messageToBeSent)
        # update the message counter
        self.counter += 1
        # print the info in the terminal window that is running the publisher node
        self.get_logger().info('Published Message: "%s"' % messageToBeSent.data)

def main(args=None):
    rclpy.init(args=args)
    publisherNode = PublisherNode()
    rclpy.spin(publisherNode)
    publisherNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()