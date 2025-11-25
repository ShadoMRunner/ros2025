#!/usr/bin/env python3
import rospy

if __name__ == "__main__":
    rospy.init_node('params_study')
    
    # Получение параметров
    distro = rospy.get_param('/rosdistro')
    rospy.loginfo("Rosdistro: %s", distro)
    
    # Попробуем получить параметр с default значением
    my_set_param = rospy.get_param('my_set', {'P': 0.0, 'I': 0.0, 'D': 0.0})
    rospy.loginfo("My set param: %s", my_set_param)
    
    # Установка параметров
    rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
    rospy.set_param('ros_loc_param', 'Hi, I am local =)')
    rospy.set_param('/ros_glob_param', 'Hi, I am global =)')
    
    # Проверка существования и удаление
    if rospy.has_param('/ros_glob_param'):
        rospy.loginfo("Global parameter exists")
        rospy.delete_param('/ros_glob_param')
        rospy.loginfo("Global parameter deleted")
    
    # Получение списка параметров
    param_list = rospy.get_param_names()
    rospy.loginfo("Parameter names: %s", param_list)
