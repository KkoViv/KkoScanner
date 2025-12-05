# thsi function retrieves the claimant IP address

import socket
import ipaddress
from socket import AF_INET, SOCK_DGRAM, IPPROTO_UDP
from colorama import Fore, Style, init
from bye_bye import bye_bye

###################################
# Retrieve the Source IP
###################################

def my_ip_function():
    
    init(autoreset=True)                                # reset style and color
    
    attempt = 0

    while True:
        
        try:
            fake_sock = socket.socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
            fake_sock.connect(('8.8.8.8', 80))
            my_ip = fake_sock.getsockname()[0]
            fake_sock.close()
            return my_ip
        
        except OSError:

            attempt += 1
            if attempt == 3:
                
                print(f"\n{Fore.YELLOW}--------------------------{Style.RESET_ALL}")
                print(f"{Fore.RED}Impossible to set automatically the source ip address{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}--------------------------{Style.RESET_ALL}")

                while True:
                    my_ip = input(f"\nEnter your IP if you want set manually it or '{Fore.YELLOW}{Style.BRIGHT}q{Style.RESET_ALL}' to exit: ").lower()

                    if my_ip == 'q':
                        bye_bye()
                    else:
                        try:
                            check_it = ipaddress.ip_address(my_ip)
                            return my_ip
                        
                        except ValueError:
                            print(f"{Fore.YELLOW}{my_ip}{Style.RESET_ALL} is not a valid IP address.")

