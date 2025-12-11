# this file is responsbile to create sorted_dict and scan_list

###################################
# IMPORTED MODULES
###################################

###################################
# CORE FUNCTION
###################################

def create_list_dict(scan_data):

    if scan_data.port_list[0] == "s":
        scan_data.scan_list = [scan_data.port_list[1]]
        scan_data.sorted_dict[scan_data.scan_list[0]] = [None, None]
        scan_data.error_response[scan_data.scan_list[0]] = [None, None, ";", None, ";", None, ";", None, None]

    
    elif scan_data.port_list[0] == "r":
        for x in range(scan_data.port_list[1], scan_data.port_list[2]+1):
            scan_data.scan_list.append(x)
            scan_data.sorted_dict[x] = [None, None]
            scan_data.error_response[scan_data.scan_list[x]] = [None, None, ";", None, ";", None, ";", None, None]


    elif scan_data.port_list[0] == "a":
        for z in range(1, 65536):
            scan_data.scan_list.append(z)
            scan_data.sorted_dict[z] = [None, None]
            scan_data.error_response[scan_data.scan_list[z]] = [None, None, ";", None, ";", None, ";", None, None]

    
    elif scan_data.port_list[0] == "p":
        for y in scan_data.port_list:
            scan_data.scan_list.append(y)
        
        scan_data.scan_list.pop(0)
        scan_data.scan_list.sort()
        
        for t in scan_data.scan_list:
            scan_data.sorted_dict[t] = [None, None]
            scan_data.error_response[scan_data.scan_list[t]] = [None, None, ";", None, ";", None, ";", None, None]



        
        