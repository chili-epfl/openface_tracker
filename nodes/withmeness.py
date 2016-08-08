#!/usr/bin/env python
#coding: utf-8

import sys
import time
import rospy
import json
from std_msgs.msg import String, Empty, Float64

pub_withmeness = rospy.Publisher('withmeness_topic', Float64, queue_size=1)

current_task = "WAITING_FOR_WORD"
current_target = "_"
value = 0.5
mu = 0.1

def onChangeTask(msg):
    global current_task
    current_task = (str)(msg.data)

def onChangeTarget(msg):
    global current_target
    current_target = (str)(msg.data)

if __name__=='__main__':

    global withmeness_value

    rospy.init_node("withmeness")

    test = rospy.search_param("targets")
    target_list = rospy.get_param(test)
    with open(target_list) as target_list_json:
        task_targets = json.load(target_list_json)

    while(True):
        # get current task:
        rospy.Subscriber("state_activity", String, onChangeTask)

        # get current target:
        rospy.Subscriber("actual_focus_of_attention", String, onChangeTarget)

        # compute EMA of online-with_me_ness:
        if current_task in task_targets:
            if current_target in task_targets[current_task]:
                value = (1-mu)*value + mu
            else:
                if current_target!="" and current_target!="_":
                    value = (1-mu)*value

        msg = Float64()
        msg.data = value
        pub_withmeness.publish(msg)

        rospy.sleep(1.0)

    rospy.spin()
