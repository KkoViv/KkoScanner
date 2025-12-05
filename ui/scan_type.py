# this file defines the type of scan the user wants to perform

###########################
# Fixs
###########################

# 1/12/25   return scan_list[o_or_h] >>> return o_or_h

###########################
# Imported Module
###########################

from colorama import Fore, Back, init, Style
from bye_bye import bye_bye

###################################
# RESET COLORAMA STYLE
###################################

init(autoreset=True)                                    # reset the colorama setting

###########################
# core function
###########################

def scan_type():

    scan_list = {                                       # store possible options
        'o' : "Open Scan",
        'h' : "Half-Open Scan"
    }                         

    print(f"\nThis program provides two different types of scan:")
    print(f"\n>>> {Fore.GREEN}Open scan{Style.RESET_ALL}: the program sends a packet with the SYN flag set and waits for a response.")
    print  (f"    if the port is open, it replies with a SYN/ACK and establishes a full TCP connection.")
    print(f"\n>>> {Fore.GREEN}Half-Open scan{Style.RESET_ALL}: The program sends a packet with the SYN flag set and waits for a response.")
    print  (f"    If the port is open, it replies with a SYN/ACK, and the scanner immediately sends a RST to")
    print  (f"    terminate the connection before it's fully established.")
    print(f"{Fore.RED}{Style.BRIGHT}!!!{Style.RESET_ALL} The Half-Scan is stealthier than the Open scan.")
    
    while True:
        o_or_h = input(f"\nSelect '{Fore.YELLOW}o{Style.RESET_ALL}' for Open, '{Fore.YELLOW}h{Style.RESET_ALL}' for half-open, '{Fore.YELLOW}q{Style.RESET_ALL}' to exit: ").lower()

        if o_or_h == 'q':
            bye_bye()
        elif o_or_h in scan_list:
            return o_or_h
        else:
            print("\nPlease enter a valid option!")
