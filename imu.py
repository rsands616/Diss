#!/usr/bin/env python


# ------------------------------------------------------------------------
#/opt/ros/kinetic/lib/python2.7/dist-packages/nav_msgs/msg$ 
#__slots__


import rospy

from sensor_msgs.msg import Imu #voltage curent both float32

# ------------------------------------------------------------------------

#def battery_callback(environment_data):
#     rospy.loginfo('Supply Voltage (V) : %s', environment_data.voltage)
#     rospy.loginfo('Supply Current (A) : %s', environment_data.current)

#    header_file.write( '-------------------------\n' + str(environment_data.header) + '\n-------------------------\n')
#    pose_file.write( '-------------------------\n' + str(environment_data.pose) + '\n-------------------------\n')
#    twist_file.write( '-------------------------\n' + str(environment_data.twist) + '\n-------------------------\n')
#    child_frame_id_file.write( '-------------------------\n' + str(environment_data.child_frame_id) + '\n-------------------------\n')

def imu_callback(environment_data):
    rospy.loginfo('Linear Acceleration \n%s\n------------------', environment_data.linear_acceleration)

#def nav_callback(environment_data):
#    rospy.loginfo('GPS Coordinates : '+ environment_data.latitude + ' ' + environment_data.longitude)

#def mag_callback(environment_data):
#    rospy.loginfo('Magnetic Field (?) : %s', environment_data.magnetic_field)


def listen():
    rospy.init_node('imu', anonymous=True)
#    rospy.Subscriber('/mavros/battery', BatteryState, battery_callback)
    rospy.Subscriber('/mavros/imu/data', Imu, imu_callback)
#    rospy.Subscriber('/mavros/gloabal_position/global', NavSatFix, nav_callback)
#    rospy.Subscriber('/mavros/imu/mag', MagneticField, mag_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listen()
