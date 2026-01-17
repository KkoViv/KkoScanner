# this file is responsible to read the data received and tell how to handle the handshake

###################################
# IMPORTED MODULES
###################################

import struct
import socket
import time
from colorama import Fore, Style
from core.send_response import send_response
from netlib.flag_bytes import flag_bytes
# TODO add send_response

def read_response(scan_data, data):

###################################
# Received IP header unpacking to check IP header lenght
###################################

    recv_ver_ihl = struct.unpack('!B', data[:1])[0] # extract the first byte

    recv_IP_version = recv_ver_ihl >> 4            # shift to right in oorder to obtain the first nibble 
    recv_IHL = recv_ver_ihl & 0x0F              # and bitwise in order to obtain the second nibble

    src_ip_raw = data[12:16]
    src_ip = socket.inet_ntoa(src_ip_raw)

    if recv_IHL > 15:
        scan_data.malformed_pack += 1       # increase errors counter
        return             # stop the runtime 

    recv_IP_header = recv_IHL * 4                # define the IP header length

    if len(data) < recv_IP_header + 20:
        scan_data.short_pack += 1
        return

################################### 
# unpack the tcp header
###################################


    try:
    
        recv_offset_flags = struct.unpack('!H', data[recv_IP_header+12:recv_IP_header+14])[0]       # unpack the offset/flags 2 bytes;
        recv_s_port, recv_d_port, recv_seq_num, recv_ack, recv_len_flags, recv_win_s, recv_tcp_check, recv_urg_p = struct.unpack('!HHLLHHHH', data[recv_IP_header:recv_IP_header + 20])
    
    except struct.error:
        scan_data.malformed_pack += 1
        return

    flags = recv_len_flags & 0x1FF                        # retrieve lat 6 bits (flags)

    f_urg = bool(flags & 0x20)
    f_ack = bool(flags & 0x10)
    f_psh = bool(flags & 0x8)
    f_rst = bool(flags & 0x4)
    f_syn = bool(flags & 0x2)
    f_fin = bool(flags & 0x1)

    # TODO delete it in production
    print(f_urg,f_ack,f_psh,f_rst,f_syn,f_fin, src_ip, recv_s_port) # debug and future uses

    # TODO replace the call of open scan with send_response when we need to send ACK/FIN/RST


    if recv_s_port in scan_data.sorted_dict:

        if (f_syn == True) and (f_ack == True):
            scan_data.sorted_dict[recv_s_port] =["Open", None]
           
            if scan_data.type_scan == 'o':
                with scan_data.semaphore:              # set scan_data.semaphore to use open scan (with)
                    flag_set = flag_bytes('ACK')        # call flag_set passing ACK return flag_set
                    send_response(scan_data, recv_s_port, flag_set) # send ack calling openscan passing scan_data, recv_s_port, flag_set):
                    time.sleep(0.1)                     #little time.out
                    flag_set2 = flag_bytes('FIN')       # call flag_set passing FIN return flag_set
                    send_response(scan_data, recv_s_port, flag_set2) # send FIN calling openscan passing scan_data, recv_s_port, flag_set):
            elif scan_data.type_scan == 'h':
                with scan_data.semaphore:              # set scan_data.semaphore to use open scan (with)                   
                    flag_set3 = flag_bytes('RST')       # call flag_set passing RST return flag_set
                    send_response(scan_data, recv_s_port, flag_set3)   # send rst calling openscan passing scan_data, recv_s_port, flag_set):

        elif f_rst == True:
            scan_data.sorted_dict[recv_s_port] = ["Closed", None]
        else:
            unusual_flags = f"URG = {f_urg}, ACK = {f_ack}, PSH = {f_psh}, RST = {f_rst}, SYN = {f_syn}, FIN = {f_fin}"
            scan_data.sorted_dict[recv_s_port] = [unusual_flags, None]
            with scan_data.semaphore:              # set scan_data.semaphore to use open scan (with)                   
                flag_set3 = flag_bytes('RST')       # call flag_set passing RST return flag_set
                send_response(scan_data, recv_s_port, flag_set3)   # send rstcalling openscan passing scan_data, recv_s_port, flag_set):
    
    else:
        scan_data.sorted_dict[recv_s_port] = ["Unexpected response from this port" , None]
        with scan_data.semaphore:              # set scan_data.semaphore to use open scan (with)                   
            flag_set3 = flag_bytes('RST')       # call flag_set passing RST return flag_set
            send_response(scan_data, recv_s_port, flag_set3)   # send rst calling openscan passing scan_data, recv_s_port, flag_set):

