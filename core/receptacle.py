# this file is responsible to:
#   receive all incoming packets
#   pass them to read_response

###################################
# IMPORTED MODULES/FUNCTION
###################################

import socket
import time
from core.read_response import read_response
from ui.bye_bye import bye_bye
from colorama import Fore, Style

###################################
# IMPORTED MODULES/FUNCTION
###################################

def receptacle (scan_data, stop_continue):

    attempt = 0
    
    while True:
    
        try:
            answer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)# open the socket for the answer
            break

        except OSError as error:
            attempt += 1
            time.sleep(1) # add a little time before to try again

            if attempt == 3:

                print(f"{Fore.RED}{Style.BRIGHT}!!! !!! !!!{Style.RESET_ALL}")
                print(f"{Fore.WHITE}>>> >>> We failed to create the socket : {Fore.YELLOW}{error}{Style.RESET_ALL}")
                print(f"{Fore.RED}{Style.BRIGHT}!!! !!! !!!{Style.RESET_ALL}")
                bye_bye()

    while stop_continue.is_set():
        
        try:

            data, addr = answer.recvfrom(65535)                  # receive answers         
            if addr[0] != scan_data.target_ip:                         # check if the answer is from the target_IP
                continue                                                # drop the answer    
            else:
                with scan_data.semaphore:                           # wait if the limit of thread is reached
                    read_response(scan_data, data)                      # call the read_response
        
        except OSError as error:
            scan_data.recv_pack_errors += 1
            continue

    answer.close()