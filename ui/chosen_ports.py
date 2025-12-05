# This function ask to choose which ports to attack


###################################
# IMPORTED MODULES/Function
###################################

from colorama import Fore, Style, Back, init
from bye_bye import bye_bye

###################################
# Core function
###################################

def chosen_ports():

    range_type = ('s', 'r' ,'p' ,'a')                           # list of possible choices

    print(f"To define which ports you want to scan, you can choose different options:")
    print(f"\nScan a single port = {Fore.YELLOW}{Style.BRIGHT}s{Style.RESET_ALL}")
    print(f"Scan a range of ports = {Fore.YELLOW}{Style.BRIGHT}r{Style.RESET_ALL}")
    print(f"Scan a pool of ports = {Fore.YELLOW}{Style.BRIGHT}p{Style.RESET_ALL}")
    print(f"Scan all ports = {Fore.YELLOW}{Style.BRIGHT}a{Style.RESET_ALL}")

    while True:
        decision = input(f"\nWhich options do you choose? ('{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' for exit)")
        decision = decision.lower()
        if decision == 'q':
            bye_bye()
        else:
            if decision in range_type:
                return decision
            else:
                print(f"{Fore.RED}Please enter a valid choice!{Style.RESET_ALL}")
                print(f"\nScan a single port = {Fore.YELLOW}{Style.BRIGHT}s{Style.RESET_ALL}")
                print(f"Scan a range of ports = {Fore.YELLOW}{Style.BRIGHT}r{Style.RESET_ALL}")
                print(f"Scan a pool of ports = {Fore.YELLOW}{Style.BRIGHT}p{Style.RESET_ALL}")
                print(f"Scan all ports = {Fore.YELLOW}{Style.BRIGHT}a{Style.RESET_ALL}")








