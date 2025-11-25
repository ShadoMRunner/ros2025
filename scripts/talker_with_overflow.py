#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker_with_overflow():
    rospy.init_node('talker_with_overflow')
    pub = rospy.Publisher('chat_topic', String, queue_size=10)
    overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    count = 0
    
    while not rospy.is_shutdown():
        hello_str = f"Message {count} at {rospy.get_time()}"
        rospy.loginfo(hello_str)
        
        msg = String()
        msg.data = hello_str
        pub.publish(msg)
        
        # Проверка на overflow
        if count >= 100:
            overflow_msg = String()
            overflow_msg.data = f"OVERFLOW! Count reached {count}"
            overflow_pub.publish(overflow_msg)
            rospy.logwarn(overflow_msg.data)
            count = 0  # Сброс счетчика
        
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_with_overflow()
    except rospy.ROSInterruptException:
        pass    
