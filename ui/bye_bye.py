###################################
# IMPORTED MODULES
###################################

import sys                                              # import sys module to handle argument
from colorama import Fore, Style, Back, init            # import colorama to handle output

###################################
# exit message 
###################################

def bye_bye():
    
    print("")
    print(f"{Fore.GREEN}{Style.BRIGHT}Good Bye!!!{Fore.RESET}{Style.RESET_ALL}")
    print(Style.RESET_ALL, end="")
    sys.exit() 