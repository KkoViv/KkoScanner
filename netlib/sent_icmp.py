###################################
# IMPORTED MODULES
###################################

import socket                                           # to manage socket creation
import time         
from socket import AF_INET, SOCK_RAW, IPPROTO_ICMP      # to manage delivery of messages
from colorama import Fore, Style, Back, init            # import colorama to handle output

###################################
# RESET COLORAMA STYLE
###################################

init(autoreset=True)                                    # reset the colorama setting

###################################
# Function
###################################

def sent_icmp(target_ip, icmp_value):

    try:                                                     # try create the socket
        sock = socket.socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
    except OSError as g_error:                       # handle exceptions
        print(f"{Fore.RED}{Style.BRIGHT}----------------------------{Style.RESET_ALL}") # display errors
        print(f"{Fore.RED}{Style.BRIGHT}Socket creation failed!!!{Style.RESET_ALL} {Fore.YELLOW}{g_error}")
        print(f"{Fore.RED}{Style.BRIGHT}----------------------------{Style.RESET_ALL}")
        return False
  
    try:
        sock.sendto(icmp_value, (target_ip, 0))          # send ICMP
    
    except OSError:                                # handel errors
        sock.close()   
        return False
       
    try:                                        
        sock.settimeout(1)                  # set waiting time for an answer
        answer, target = sock.recvfrom(2048)   # receive response
        sock.close()   
        return True

    except socket.timeout:
        sock.close()   
        return False

    except OSError:                                # handel errors
        sock.close()       
        return False



