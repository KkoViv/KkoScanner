# this file provides the bytes related to the flags in TCP packet

def flag_bytes(flag_s):
    
    if flag_s == "SYN": # DELETE IT " 'Open Scan' or flag_s == 'Half-Open Scan'
        set_flag = 0b0101000000000010 # 2 bytes (4/6/0/0/0/0/1/0 bits) H
    elif flag_s == "RST":
        set_flag = 0b0101000000000100 # 2 bytes (4/6/0/0/0/1/0/0 bits) H
    elif flag_s == "FIN":
        set_flag = 0b0101000000000001 # 2 bytes (4/6/0/0/0/0/0/1 bits) H
    elif flag_s == "ACK":
        set_flag = 0b0101000000010000 # 2 bytes (4/6/0/1/0/0/1/0 bits) H

    return set_flag

''' other flags and set manually 
    else:
        print("here a loop to ask the user to set manually flags")'''

