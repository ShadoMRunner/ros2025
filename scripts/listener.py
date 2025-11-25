#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"I heard: {msg.data}")

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('chat_topic', String, callback, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
