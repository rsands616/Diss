#!/usr/bin/env python


# ------------------------------------------------------------------------

import rospy
#from nav_msgs.msg import Odometry #old
#from mavros_msgs.msg import  Altitude #altitude amsl relative both float32
from sensor_msgs.msg import BatteryState #voltage curent both float32
#from sensor_msgs.msg import  Imu #linear_acceleration as geometry_msgs/Vector3'
#from sensor_msgs.msg import  NavSatFix #latitude longitude float64
#from sensor_msgs.msg import  MagneticField  #magnetic_field    geometry_msgs/Vector3
# ------------------------------------------------------------------------

def battery_callback(environment_data):
     rospy.loginfo('Supply Voltage (V) : %s', environment_data.voltage)
     rospy.loginfo('Supply Current (A) : %s \n ---------------------', environment_data.current)
     


def listen():
    rospy.init_node('imu', anonymous=True)
    rospy.Subscriber('/mavros/battery', BatteryState, battery_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listen()
