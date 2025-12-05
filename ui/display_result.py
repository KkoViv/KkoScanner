# this function simple diyplay the output

from colorama import Fore, Style

def display_result(scan_data):

    for port, result in scan_data.sorted_dict.items():
        status = result[0]
        print( f"Port n°{Fore.GREEN}{port}{Style.RESET_ALL} is {Fore.GREEN}{status}{Style.RESET_ALL}")
