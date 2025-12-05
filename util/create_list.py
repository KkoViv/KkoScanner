# this file receives the list info and return a list the first element is list info 

###################################
# IMPORTED MODULES/Function
###################################

from colorama import Fore, Style, Back, init
from bye_bye import bye_bye

###################################
# Core function
###################################

def create_list(type_l):

    port_list = [type_l]

    if type_l == 's':
        while True:
            first_e = input(f"\nPlease enter the port you want scan: '{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' to exit ")
            if first_e.lower() == 'q':
                bye_bye()
            else:
                try:
                    first_e = int(first_e)
                    if first_e in range (1,65536):
                        port_list.append(first_e)
                        return port_list
                    else:
                        print(f"{Fore.YELLOW}Port must be in the range of 1-65535.{Style.RESET_ALL}")
                except ValueError as er:
                        print(f"{Fore.YELLOW}An error occurred:{Fore.RED} {er}{Style.RESET_ALL}")
###########################
    elif type_l == 'r':
        while True:                                         # retrieve the start of the range
            start_e = input(f"\nPlease enter the start of your range: '{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' to exit ")
            if start_e.lower() == 'q':
                bye_bye()
            else:
                try:
                    start_e = int(start_e)
                    if start_e in range (1,65536):
                        port_list.append(start_e)
                        break
                    else:
                        print(f"{Fore.YELLOW}Port must be in the range of 1-65535.{Style.RESET_ALL}")
                except ValueError as er:
                        print(f"{Fore.YELLOW}An error occurred:{Fore.RED} {er}{Style.RESET_ALL}")
        
        while True:                                         # retrieve the end of the range
            end_e = input(f"\nPlease enter the end of your range: '{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' to exit ")
            if end_e.lower() == 'q':
                bye_bye()
            else:
                try:
                    end_e = int(end_e)
                    if end_e in range (1,65536):
                        if end_e > start_e:
                            port_list.append(end_e)
                            return port_list
                        else:
                            print(f"{Fore.YELLOW}The end of range must be greater that {start_e}.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}Port must be in the range of 1-65535.{Style.RESET_ALL}")
                except ValueError as er:
                        print(f"{Fore.YELLOW}An error occurred:{Fore.RED} {er}{Style.RESET_ALL}")
###########################
    elif type_l == 'p':                             # retrieve a pool of ports
        while True:
            pool_v = input(f"\nPlease enter a port to scan: '{Fore.YELLOW}{Style.BRIGHT}0{Style.RESET_ALL}' to end the list, '{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' for exit ")
            if pool_v == 'q':
                bye_bye()
            else:
                try:
                    pool_v = int(pool_v)
                    if pool_v == 0:
                        if len(port_list) == 1:
                            print(f"Your ports list is empty. Please provide valid inputs or exit!")
                            #pool_v = input(f"Your ports list is empty. Please provide valid inputs or exit!")
                            continue
                        else:
                            return port_list
                    elif pool_v in range (1,65536):
                        if pool_v not in port_list:
                            port_list.append(pool_v)
                            continue
                        else:
                            print(f"{Fore.YELLOW}{pool_v} is already in your pool.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}Port must be in the range of 1-65535.{Style.RESET_ALL}")
                except ValueError as er:
                    print(f"{Fore.YELLOW}An error occurred:{Fore.RED} {er}{Style.RESET_ALL}")
###########################
    elif type_l == 'a':
        port_list = [type_l, 1, 65536]
        return port_list




        
        