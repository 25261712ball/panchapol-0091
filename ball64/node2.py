#!/usr/bin/env python3

import rospy
from sed_msgs.msg import String

def run(val):
	if val.data == "hello":
		rospy.loginfo("Sawaddee i brod ")
	else:
		rospy.loginfo("No")
		
if __name__=="__main__":
	sub = rospy.Subscriber("chatter",String,Callblack=run)
	rospy.init_node("Listener")
	rospy.spin()
