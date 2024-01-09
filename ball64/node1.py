#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def run(val):
	if val.data == "Hello world":
		rospy.loginfo("Node1: " + "Hello world to")
	else:
		rospy.loginfo("Node1: " +" No ")
		
if __name__=="__main__":
	sub = rospy.Subscriber("chatter",String,callback=run)
	rospy.init_node("Listener")
	rospy.spin()
