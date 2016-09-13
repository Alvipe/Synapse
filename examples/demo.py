# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 02:05:48 2016

@author: alvaro
"""

# These two lines are not needed if the Synapse module is in the same directory as this script
import sys
sys.path.append("../src/Python")

import synapse

if hasattr(__builtins__, 'raw_input'):
    input = raw_input

serial_port_list = synapse.scan_ports()
ser, status = synapse.connect(serial_port_list[0])
if status:
    print "Connected!"
else:
    print "Connection error"

while(1):
    data_list =[]
    command = input("Do you want to (s)end or to (r)eceive data?: ")
    if command == 's':
        ser.write(command)
        action = input("What do you want to do, (c)lose or (o)pen the hand?: ")
        if action == 'c':
            set_point_list = [10.0,11.1,12.2,13.3,14.4,15.5]
        elif action == 'o':
            set_point_list = [10.0,0.0,0.0,0.0,0.0,0.0]
        message = synapse.send_setpoint_list(ser,set_point_list)
    elif command == 'r':
        ser.write(command)
        data_list = synapse.get_data(ser)
        if(data_list[0]==10.0 and data_list[1]==11.1 and data_list[2]==12.2 and data_list[3]==13.3 and data_list[4]==14.4 and data_list[5]==15.5):
            print("Oh yeah!")
        else:
            print("Oh no!")
