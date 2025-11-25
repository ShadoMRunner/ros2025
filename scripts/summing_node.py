#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray, Float32

def callback(data):
    # Суммируем три числа
    if len(data.data) == 3:
        total = sum(data.data)
        pub.publish(Float32(data=total))
        rospy.loginfo("Summing: input %s, output %f", data.data, total)

if __name__ == '__main__':
    rospy.init_node('summing')
    pub = rospy.Publisher('/response', Float32, queue_size=10)
    rospy.Subscriber('/intermediate', Float32MultiArray, callback)
    rospy.loginfo("Summing node started")
    rospy.spin()
    
