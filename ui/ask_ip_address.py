# This function ask the user to insert a Ip_address
# check if the IP address is valid
# return the ip address


###################################
# NEEDED MODULES
###################################

from colorama import Fore,Style,init,Back               # set the output color etc etc
import ipaddress                                        # to check valid ip address 
from bye_bye import bye_bye                              # exit kindly
from ping import ping

###################################
# Ask user input for IP Address and check it
###################################

def ask_ip_address():

    init(autoreset=True)                                # reset style and color

    while True:
        your_target = input(f"\nPlease insert the target IP address: ({Fore.YELLOW}'q' to exit{Style.RESET_ALL}) ")
        if your_target.lower() == 'q':                  # exit the program
            bye_bye()

        try:
            check_ip = bool(ipaddress.ip_address(your_target))  # check the provided IP address
            
            if check_ip:
                ping_result = ping(your_target)           # call the function to perform ping passing to it the IP address
                
                if ping_result == True:              # if the function return a True state host reachable
                    print(f"The {Fore.GREEN}{Style.BRIGHT}{your_target}{Style.RESET_ALL} IP Address is valid and reachable!")
                    return your_target
                else:
                    print(f"\n{Fore.RED}{Style.BRIGHT}!!!{Style.RESET_ALL} The target seems unreachable.")# inform user about hte host unreachable
                    print(f"    We can't know if the host is offline or instead the network filters the ping packets.")
                    print(f"\nYou can select:")
                    print(f"{Fore.YELLOW}'c'{Style.RESET_ALL} to perform the scan against {Fore.GREEN}{your_target}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}'i'{Style.RESET_ALL} to insert a different IP Address")
                    print(f"{Fore.YELLOW}'q'{Style.RESET_ALL} to quit the program")
                    ping_choice = input(f"\nType your choice: ").lower()               # ask to the user if he wants to continue 'c', quit 'q', insert a new ipaddress
                    
                    if ping_choice == 'q':
                        bye_bye()
                    elif ping_choice == "c":
                        return your_target
                    else:
                        continue

        except ValueError:
            print(f"{Fore.YELLOW}{your_target}{Style.RESET_ALL} is not a valid IP address.")

                 
