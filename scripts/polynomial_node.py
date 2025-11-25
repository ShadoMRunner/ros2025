#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    # Получаем три числа и возводим в степень
    if len(data.data) == 3:
        a, b, c = data.data
        # Возводим в степени: 1-е число^2, 2-е число^3, 3-е число^4
        result = [a**2, b**3, c**4]
        pub.publish(Float32MultiArray(data=result))
        rospy.loginfo("Polynomial: input %s, output %s", data.data, result)

if __name__ == '__main__':
    rospy.init_node('polynomial')
    pub = rospy.Publisher('/intermediate', Float32MultiArray, queue_size=10)
    rospy.Subscriber('/request', Float32MultiArray, callback)
    rospy.loginfo("Polynomial node started")
    rospy.spin()
