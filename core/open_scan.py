# This file handle a OPEN Scan

###################################
# IMPORTED MODULES/FUNCTION
###################################

import time
import socket
from socket import AF_INET, IPPROTO_RAW, IPPROTO_TCP, SOCK_RAW
from packet_craft import packet_craft

###################################
# CORE FUNCTION
###################################

def open_scan(scan_data, port, flag_set):

    sock = None

    try:
        with scan_data.semaphore:

            attempt = 0
            
            while True:

                try:
                    
                    sock = socket.socket(AF_INET, SOCK_RAW, IPPROTO_RAW) # create the socket                                     
                    break

                except Exception:
                    attempt += 1
                    time.sleep(0.2) # add a little time before to try again
                    if attempt == 3:
                        scan_data.sorted_dict[port] = ["Something went wrong during socket creation", None]
                        return None

            attempt = 0

            while True:

                try:
                    
                    packet_s = packet_craft(scan_data.target_ip, port, flag_set, scan_data.my_ip) # creates the packet
                    break

                except Exception:
                    attempt += 1
                    time.sleep(0.2) # add a little time before to try again
                    if attempt == 3:
                        scan_data.sorted_dict[port] = ["Something went wrong during packet creation", None]
                        return None

            attempt = 0

            while True:

                try:
                    
                    sock.sendto(packet_s, (scan_data.target_ip, port)) # send the socket
                    break

                except Exception:
                    attempt += 1
                    time.sleep(0.2) # add a little time before to try again
                    if attempt == 3:
                        scan_data.sorted_dict[port] = ["Something went wrong sending the packet", None]
                        return None
    finally:
        if sock is not None:
            sock.close()