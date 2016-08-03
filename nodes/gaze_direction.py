#!/usr/bin/env python
#coding: utf-8

import rospy
import os
import numpy as np
import sys
import time

from geometry_msgs.msg import PointStamped
from std_msgs.msg import String, Empty, Header, Float32MultiArray
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
import tf

br = tf.TransformBroadcaster()

def onReceiveDirection(msg):
    x = msg.data[0]/100.
    y = msg.data[1]/100.
    z = msg.data[2]/100.
    a = msg.data[3]
    b = msg.data[4]
    c = msg.data[5]
    w = 0
    rospy.loginfo(str(x)+" , "+str(y)+" , "+str(z)+" , "+str(a)+" , "+str(b)+" , "+str(c))
    #br.sendTransform((x,y,z),(a,b,c,w),rospy.Time.now(),"face_0","base_footprint")


if __name__=="__main__":

    rospy.init_node("gaze_direction")

    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        rospy.Subscriber("topic_features", Float32MultiArray, onReceiveDirection)
        rate.sleep()
