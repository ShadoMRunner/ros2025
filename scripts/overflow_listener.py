#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.logwarn(f"OVERFLOW DETECTED: {msg.data}")

def overflow_listener():
    rospy.init_node('overflow_listener')
    rospy.Subscriber('overflow_topic', String, overflow_callback, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    overflow_listener()
