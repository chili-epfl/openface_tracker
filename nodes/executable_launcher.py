#!/usr/bin/env python
#coding: utf-8

################################################################################################
## this node is a remote control allowing manual modification of several parameters as
## well as the manual start of a animation
################################################################################################

import rospy
import os

if __name__ == '__main__':
	rospy.init_node('executable_launcher')

	# get current open face face
	path = rospy.get_param('~pathOpenFace', '/home/alexis/catkin/src/features_face/OpenFace')
	path += '/build/bin/FeatureExtraction'

	os.system(path)
