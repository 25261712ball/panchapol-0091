#!/usr/bin/env python3

from tkinter import *
import rospy
from geometry_msgs.msg import Twist  # Correct import for Twist
#from std_msgs.msg import Empty
from std_srvs.srv import Empty

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

cmd = Twist()

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x200")



def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x =cmd.linear.x + 0.7
	cmd.angular.z= 0.0
	pub.publish(cmd)
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x =cmd.linear.x - 0.7
	cmd.angular.z = 0.0
	pub.publish(cmd)

def lt():
	print("lt")
	cmd = Twist()
	cmd.linear.y =  0.7
	cmd.angular.z=  0.0
	pub.publish(cmd)
def rt():
	print("rt")
	cmd = Twist()
	cmd.linear.y = -0.7
	cmd.angular.z= 0.0
	pub.publish(cmd)
def rt2():
	print("rt2")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= -0.7
	pub.publish(cmd)
def lt2():
	print("rt2")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= 0.7
	pub.publish(cmd)
def reset():
    print("reset")
    rospy.wait_for_service("reset")
    clear_bg = rospy.ServiceProxy("reset", Empty)
    clear_bg()
    
	

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

B_reset = Button(text="Reset", command=reset)
B_reset.place(x=73, y=80)

B5 = Button(text = "RT2", command=rt2)
B5.place(x=128, y=130)

B6 = Button(text = "LT2", command=lt2)
B6.place(x=20, y=130)

frame.mainloop()
