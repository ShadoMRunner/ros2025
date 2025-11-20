#!/usr/bin/env python3
import rospy
import datetime
import time

def main():
    rospy.init_node('time_node', anonymous=True)
    rate = rospy.Rate(0.2)  # 0.2 Hz = каждые 5 секунд
    
    while not rospy.is_shutdown():
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        rospy.loginfo(f"Current time: {formatted_time}")
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
