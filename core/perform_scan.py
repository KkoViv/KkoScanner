# this file starts the scanning

###################################
# NEEDED MODULES/FUNCTIONS
###################################

import time
import random
import socket
import threading
from netlib.packet_craft import packet_craft
from core.open_scan import open_scan
from core.receptacle import receptacle

###################################
# CORE FUNCTION
###################################

# TODO insert a instruction to retrieve the time stamp when invoke open_scan to put in Active_phase_resume


def perform_scan(scan_data):
    print(scan_data.type_scan)  # reference only DELETE in the final version

    threads = []                        # open the thread list
    
    stop_continue = threading.Event()   # create the boolean event
    stop_continue.set()                 # set it as True
    
    t_receptacle = threading.Thread(target=receptacle, args=(scan_data, stop_continue))      # create a thread with the receptacle                  
    threads.append(t_receptacle)
    t_receptacle.start()

    mode = scan_data.port_list[0]
   
    flag_set = "SYN"

    if mode == 's':
        open_scan(scan_data, scan_data.port_list[1], flag_set)                     # return the port status
        time_out = (time.time() +30 )                 # take the current time
        
    elif mode == 'r':

        port_list = []   		# port_list[]
        for x in range(scan_data.port_list[1],scan_data.port_list[2]+1):
            port_list.append(x)
        
        random.shuffle(port_list)						# shuffle the list 
        
        for port in port_list:							# select the port to scan
            with scan_data.semaphore:					# open a thread if semaphore is under his limit
                open_scan(scan_data, port, flag_set)   # call open_scan function(scan_data)
        time_out = (time.time() +30 ) 

    while time_out > time.time():
        continue
    
    stop_continue.clear()
    t_receptacle.join()

   #TODO add p and a option 
    '''
 
            
            # elif data.port_list == p
                # port_list = data_port_list     
                # port_list = port_list.pop(0)        # delete the first element that is not a port number
                # random.shuffle(port_list)
                # for port in port_list
                            # call open_scan function(scan_data)
                # return to main function

            # elif data.port_list == a
                # port_list[]
                # for x in range(data.port_list[1],data.port_list[2]+1)
                    # port_list.append(x)
                # random.shuffle(port_list)
                # for port in port_list
                            # call open_scan function(scan_data)
                # return to main function

    '''


