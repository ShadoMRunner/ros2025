#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray, Float32

class RequestNode:
    def __init__(self):
        self.response_received = False
        self.result = None
        
    def response_callback(self, data):
        self.response_received = True
        self.result = data.data
        rospy.loginfo("Request: received response: %f", data.data)
        
    def send_request(self, numbers):
        rospy.init_node('request', anonymous=True)
        pub = rospy.Publisher('/request', Float32MultiArray, queue_size=10)
        rospy.Subscriber('/response', Float32, self.response_callback)
        
        # Ждем подключения
        rospy.sleep(1)
        
        # Отправляем запрос
        msg = Float32MultiArray(data=numbers)
        pub.publish(msg)
        rospy.loginfo("Request: sent numbers %s", numbers)
        
        # Ждем ответа
        timeout = rospy.Duration(10)  # 10 секунд таймаут
        start_time = rospy.Time.now()
        
        while (rospy.Time.now() - start_time) < timeout and not self.response_received:
            rospy.sleep(0.1)
            
        if self.response_received:
            rospy.loginfo("Final result: %f", self.result)
        else:
            rospy.logerr("Request: timeout - no response received")
            
        rospy.signal_shutdown("Done")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: request_node.py <num1> <num2> <num3>")
        sys.exit(1)
        
    try:
        numbers = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
    except ValueError:
        print("Error: All arguments must be numbers")
        sys.exit(1)
        
    node = RequestNode()
    node.send_request(numbers)
