#! /usr/bin/python

# General pipeline:
# 1) ask IP → ask_ip_address()
# 2) ask scan type → scan_type()
# 3) choose ports → chosen_ports()
# 4) prepare list → create_list()
# 5) create dictionary → create_list_dict()
# 6) perform scan → perform_scan()
# 7) analyze packets → read_response()
# 8) results → display_result()

###################################
# IMPORTED MODULES
###################################



###################################
# IMPORTED functions
###################################

from ui.bye_bye import bye_bye
from ui.ask_ip_address import ask_ip_address
from core.scan_param_class import ScanParam
from ui.chosen_ports import chosen_ports
from util.create_list import create_list
from ui.scan_type import scan_type
# DELETE IT from flag_bytes import flag_bytes
from core.perform_scan import perform_scan
from util.my_ip_function import my_ip_function
from util.create_list_dict import create_list_dict
from ui.display_result import display_result

###################################
# MAIN FUNCTION
###################################

def main():

###################################
# Welcome user
###################################

# print the welcome banner
# !!!!!!!!!!! need check about sudo permission

    scan_data = ScanParam()                                       # create class object

    scan_data.target_ip = ask_ip_address()                        # retrieve a valid ip address target

    scan_data.my_ip = my_ip_function()                            # retrive the IP of claimant

    scan_data.port_info = chosen_ports()                          # retreive the kind of ports list the user wants to use

    scan_data.port_list = create_list(scan_data.port_info)        # fill the list of ports 

    scan_data.type_scan = scan_type()                             # retrieve the scan type

    # TODO add function to ask user how many attempts needed before to stop the active phase for single port

    create_list_dict(scan_data)                                    # create the list for scanning and the dict to store results
    
    # DELETE IT scan_data.flag_bytes = flag_bytes(scan_data.type_scan)         # set the flags TCP bytes

    perform_scan(scan_data)                                       # perform the scan

    display_result(scan_data)                                     # output

    # TODO add option to read error related to the ACK/RST/FIN packet sent

if __name__ == "__main__":
    main()
