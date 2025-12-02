#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker')
    pub = rospy.Publisher('chat_topic', String, queue_size=10)
    rate = rospy.Rate(10)  
    count = 0
    
    while not rospy.is_shutdown():
        hello_str = f"Message {count} at {rospy.get_time()}"
        rospy.loginfo(hello_str)
        
        msg = String()
        msg.data = hello_str
        pub.publish(msg)
        
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
