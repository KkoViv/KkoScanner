# This file handle a SYN Probe Delivery

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


def open_scan(scan_data, port, flag_set):

    scan_data.active_phase_resume[port]["probe_state"] = "tried"
    scan_data.active_phase_resume[port]["outcome_reason"] = "unknown_error"

    sock = None

    try:
        with scan_data.semaphore:
        
            while True:

                try:
                    
                    sock = socket.socket(AF_INET, SOCK_RAW, IPPROTO_RAW) # create the socket                                     
                    break

                except Exception as error:

                    scan_data.active_phase_resume[port]["socket_err_count"] += 1
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.active_phase_resume[port]["socket_err_count"] == scan_data.max_attempt:
                        scan_data.sorted_dict[port] = ["Something went wrong during socket creation", None]
                        scan_data.active_phase_resume[port]["active_timestamp"] = time.time()
                        scan_data.active_phase_resume[port]["probe_state"] = "failed"
                        scan_data.active_phase_resume[port]["outcome_reason"] = "socket_creation_error"
                        scan_data.active_phase_resume[port]["exception_message"] = f"{error}"

                        return None

            while True:

                try:
                    
                    packet_s = packet_craft(scan_data.target_ip, port, flag_set, scan_data.my_ip) # creates the packet
                    break

                except Exception as error:

                    scan_data.active_phase_resume[port]["packet_err_count"] += 1
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.active_phase_resume[port]["packet_err_count"] == scan_data.max_attempt:
                        scan_data.sorted_dict[port] = ["Something went wrong during packet creation", None]
                        scan_data.active_phase_resume[port]["active_timestamp"] = time.time()
                        scan_data.active_phase_resume[port]["probe_state"] = "failed"
                        scan_data.active_phase_resume[port]["outcome_reason"] = "packet_creation_error"
                        scan_data.active_phase_resume[port]["exception_message"] = f"{error}"

                        return None


            while True:

                try:
                    
                    sock.sendto(packet_s, (scan_data.target_ip, port)) # send the socket
                    break

                except Exception as error:

                    scan_data.active_phase_resume[port]["sendto_err_count"] += 1
                    time.sleep(0.2) # add a little time before to try again
                    if scan_data.active_phase_resume[port]["sendto_err_count"] == scan_data.max_attempt:
                        scan_data.sorted_dict[port] = ["Something went wrong during sendto delivery", None]
                        scan_data.active_phase_resume[port]["active_timestamp"] = time.time()
                        scan_data.active_phase_resume[port]["probe_state"] = "failed"
                        scan_data.active_phase_resume[port]["outcome_reason"] = "sendto_error"
                        scan_data.active_phase_resume[port]["exception_message"] = f"{error}"

                        return None

    except Exception as error:
        scan_data.active_phase_resume[port]["probe_state"] = "failed"
        scan_data.active_phase_resume[port]["active_timestamp"] = time.time()
        scan_data.active_phase_resume[port]["exception_message"] = f"{error}"

        return None


    finally:
        if sock is not None:
            sock.close()

    # update clean exit
    scan_data.active_phase_resume[port]["probe_state"] = "sent"
    scan_data.active_phase_resume[port]["outcome_reason"] = "success"
    scan_data.active_phase_resume[port]["exception_message"] = ""
    scan_data.active_phase_resume[port]["active_timestamp"] = time.time()

    return None