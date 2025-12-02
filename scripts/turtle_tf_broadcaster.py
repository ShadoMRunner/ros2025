#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math

# Глобальная переменная для имени черепашки
turtlename = ""

def handle_turtle_pose(msg):
    # Создаем объект для публикации TF
    br = tf.TransformBroadcaster()
    
    # Публикуем основное преобразование (world -> turtle)
    br.sendTransform(
        (msg.x, msg.y, 0),  # Смещение (x, y, z)
        quaternion_from_euler(0, 0, msg.theta),  # Поворот (кватернион)
        rospy.Time.now(),  # Временная метка
        turtlename,  # Дочерняя система координат
        "world"  # Родительская система координат
    )
    
    # ДОПОЛНИТЕЛЬНО: Публикуем преобразование для "морковки"
    # Морковка вращается вокруг черепашки
    current_time = rospy.Time.now().to_sec()
    radius = 1.0  # Радиус вращения
    angular_speed = 0.5  # Скорость вращения
    
    # Координаты морковки (круг вокруг черепашки)
    carrot_x = radius * math.cos(angular_speed * current_time)
    carrot_y = radius * math.sin(angular_speed * current_time)
    
    br.sendTransform(
        (carrot_x, carrot_y, 0),
        quaternion_from_euler(0, 0, 0),  # Без поворота
        rospy.Time.now(),
        "carrot",  # Система координат морковки
        turtlename  # Относительно черепашки
    )

if __name__ == '__main__':
    # Инициализация узла
    rospy.init_node('turtle_tf_broadcaster')
    
    # Получаем параметр с именем черепашки
    turtlename = rospy.get_param('~turtle_tf_name', 'turtle1')
    
    # Подписываемся на топик с позицией черепашки
    rospy.Subscriber(
        'input_pose',  # Имя топика (будем переназначать в launch-файле)
        Pose,
        handle_turtle_pose
    )
    
    # Работаем до завершения
    rospy.spin()
