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
        scan_data.sorted_dict[scan_data.scan_list[0]] = [None, None] # Status, banner
        scan_data.active_phase_resume[scan_data.scan_list[0]] = {        
                # Active_phase_resume dict
                # Key = port number
                # Values :
                "probe_state" : "not_attempted", #   not_attempted (default) / tried (at the beginning of open_scan)/ sent / failed
                "outcome_reason" : "never_called",        #   never_called (default) / success / unknown_error / socket_creation_error / packet_creation_error / sendto_error
                "active_timestamp" : None,      #   active_timestamp = when the task of active is marked completed sent or not.
                "exception_message" : "unknown_exception", # unknown_exception as default
                "socket_err_count" : 0,         #   socket creation error. 0 (default)
                "packet_err_count" : 0,         #   packet creation error. 0 (default)
                "sendto_err_count" : 0,         #   sendto error. 0 (default)
                }

        # TODO passive phase resume

    
    elif scan_data.port_list[0] == "r":
        for x in range(scan_data.port_list[1], scan_data.port_list[2]+1):
            scan_data.scan_list.append(x)
            scan_data.sorted_dict[x] = [None, None] # Status, banner
            scan_data.active_phase_resume[x] = {        
 
                "probe_state" : "not_attempted",
                "outcome_reason" : "never_called",    
                "active_timestamp" : None,
                "exception_message" : "unknown_exception",
                "socket_err_count" : 0,
                "packet_err_count" : 0,
                "sendto_err_count" : 0,
                }
            # TODO passive phase resume


    elif scan_data.port_list[0] == "a":
        for z in range(1, 65536):
            scan_data.scan_list.append(z)
            scan_data.sorted_dict[z] = [None, None] # Status, banner
            scan_data.active_phase_resume[z] = {        

                "probe_state" : "not_attempted",
                "outcome_reason" : "never_called",
                "active_timestamp" : None,
                "exception_message" : "unknown_exception",
                "socket_err_count" : 0,
                "packet_err_count" : 0,
                "sendto_err_count" : 0,
                }
           # TODO passive phase resume

    
    elif scan_data.port_list[0] == "p":
        for y in scan_data.port_list:
            scan_data.scan_list.append(y) 
        
        scan_data.scan_list.pop(0) # the first value is a string "p" we need to remove it in order to sort ports
        scan_data.scan_list.sort()
        
        for t in scan_data.scan_list:
            scan_data.sorted_dict[t] = [None, None] # Status, banner
            scan_data.active_phase_resume[t] = {        

                "probe_state" : "not_attempted",
                "outcome_reason" : "never_called",
                "active_timestamp" : None,
                "exception_message" : "unknown_exception",
                "socket_err_count" : 0,
                "packet_err_count" : 0,
                "sendto_err_count" : 0,
                }
            # TODO passive phase resume



        
        