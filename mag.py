#!/usr/bin/env python


# ------------------------------------------------------------------------
#/opt/ros/kinetic/lib/python2.7/dist-packages/nav_msgs/msg$ 
#__slots__

#header_file = open('../header_file.txt',"w")
#pose_file = open('../pose_file.txt',"w")
#twist_file = open('../twist_file.txt',"w")
#child_frame_id_file = open('../child_frame_id.txt',"w")
import rospy
#from nav_msgs.msg import Odometry #old
#from mavros_msgs.msg import  Altitude #altitude amsl relative both float32
from sensor_msgs.msg import MagneticField #voltage curent both float32
#from sensor_msgs.msg import  Imu #linear_acceleration as geometry_msgs/Vector3'
#from sensor_msgs.msg import  NavSatFix #latitude longitude float64
#from sensor_msgs.msg import  MagneticField  #magnetic_field    geometry_msgs/Vector3
# ------------------------------------------------------------------------


def mag_callback(environment_data):
    rospy.loginfo('Magnetic Field \n%s\n -------------------', environment_data.magnetic_field)


def listen():
    rospy.init_node('mag', anonymous=True)
    rospy.Subscriber('/mavros/imu/mag', MagneticField, mag_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listen()
