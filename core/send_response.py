# This file handle a OPEN Scan

###################################
# IMPORTED MODULES/FUNCTION
###################################

import time
import socket
from socket import AF_INET, IPPROTO_RAW, IPPROTO_TCP, SOCK_RAW
from netlib.packet_craft import packet_craft

###################################
# CORE FUNCTION
###################################

def send_response(scan_data, port, flag_set):

    scan_data.response_resume[port]["flag"] = f"{flag_set}"
    scan_data.response_resume[port]["response_state"] = "tried"
    scan_data.response_resume[port]["outcome_reason"] = "unknown_error"
    
    sock = None

    try:
        with scan_data.semaphore:
            
            while True:

                try:
                    
                    sock = socket.socket(AF_INET, SOCK_RAW, IPPROTO_RAW) # create the socket                                     
                    break

                except Exception as error:
                    scan_data.response_resume[port]["socket_err_count"] +=1 
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.response_resume[port]["socket_err_count"] == scan_data.max_attempt:
                        scan_data.response_resume[port]["response_state"] = "failed"
                        scan_data.response_resume[port]["outcome_reason"] = "socket_creation_error"
                        scan_data.response_resume[port]["timestamp"] = time.time()
                        scan_data.response_resume[port]["exception_message"] = f"{error}"
 
                        return None

            while True:

                try:
                    
                    packet_s = packet_craft(scan_data.target_ip, port, flag_set, scan_data.my_ip) # creates the packet
                    break

                except Exception as error:
                    scan_data.response_resume[port]["packet_err_count"] +=1 
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.response_resume[port]["packet_err_count"] == scan_data.max_attempt:
                        scan_data.response_resume[port]["response_state"] = "failed"
                        scan_data.response_resume[port]["outcome_reason"] = "packet_creation_error"
                        scan_data.response_resume[port]["timestamp"] = time.time()
                        scan_data.response_resume[port]["exception_message"] = f"{error}"

                        return None

            while True:

                try:
                    
                    sock.sendto(packet_s, (scan_data.target_ip, port)) # send the socket
                    break

                except Exception as error:
                    scan_data.response_resume[port]["sendto_err_count"] +=1 
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.response_resume[port]["sendto_err_count"] == scan_data.max_attempt:
                        scan_data.response_resume[port]["response_state"] = "failed"
                        scan_data.response_resume[port]["outcome_reason"] = "sendto_error"
                        scan_data.response_resume[port]["timestamp"] = time.time()
                        scan_data.response_resume[port]["exception_message"] = f"{error}"

                        return None
                    
    except Exception as error:
            scan_data.response_resume[port]["response_state"] = "failed"
            scan_data.response_resume[port]["timestamp"] = time.time()
            scan_data.response_resume[port]["exception_message"] = f"{error}"

            return None


    finally:
        if sock is not None:
            sock.close()

        # update clean exit
    scan_data.response_resume[port]["response_state"] = "sent"
    scan_data.response_resume[port]["outcome_reason"] = "success"
    scan_data.response_resume[port]["exception_message"] = None
    scan_data.response_resume[port]["timestamp"] = time.time()

    return None