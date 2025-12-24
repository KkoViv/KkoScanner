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
        scan_data.Active_phase_resume[scan_data.scan_list[0]] = ["Not attempted", None, None, 0, 0, 0]
        
        # Active_phase_resume dict
        # Key = port number
        # Values :
        #   probe_sent = Not attempted (default) / True / False
        #   outcome_reason = Sent / Socket creation error / Packet creation error / sendto error
        #   End_time_stamp = when the task of active is marked completed sent or not.
        #   error in socket creation = 0 (default)
        #   error in packet creation = 0 (default)
        #   error in sendto creation = 0 (default)
       

        # TODO passive phase resume

    
    elif scan_data.port_list[0] == "r":
        for x in range(scan_data.port_list[1], scan_data.port_list[2]+1):
            scan_data.scan_list.append(x)
            scan_data.sorted_dict[x] = [None, None] # Status, banner
            scan_data.Active_phase_resume[x] = ["Not attempted", None, None, 0, 0, 0]
            # TODO passive phase resume


    elif scan_data.port_list[0] == "a":
        for z in range(1, 65536):
            scan_data.scan_list.append(z)
            scan_data.sorted_dict[z] = [None, None] # Status, banner
            scan_data.Active_phase_resume[z] = ["Not attempted", None, None, 0, 0, 0]
           # TODO passive phase resume

    
    elif scan_data.port_list[0] == "p":
        for y in scan_data.port_list:
            scan_data.scan_list.append(y)
        
        scan_data.scan_list.pop(0)
        scan_data.scan_list.sort()
        
        for t in scan_data.scan_list:
            scan_data.sorted_dict[t] = [None, None] # Status, banner
            scan_data.Active_phase_resume[t] = ["Not attempted", None, None, 0, 0, 0]
            # TODO passive phase resume



        
        