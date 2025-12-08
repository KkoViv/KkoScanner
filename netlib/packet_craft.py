# this file is responsible to craft the IP/TCP packets

###################################
# IMPORTED MODULES/FUNCTIONS
###################################

import struct
import random
import socket
from netlib.calculate_check import calculate_check
from netlib.flag_bytes import flag_bytes

###################################
# CORE FUNCTION
###################################

def packet_craft(target_ip, target_port, set_flag, my_ip):
  
    flag_value = flag_bytes(set_flag)
        
    ###################################
    # IP packet field structutur
    ###################################

    ver_ihl = 0b01000101 # 1 byte for version and ihl
    serv_type = 224 # 1 byte for service type
    tot_l = 0               # 2 byte for total lenght placeholder
    id_pack = 1              # 2 bytes for identifier
    flag_frag = 0 # 3 bits for DF/MF flags, 13 bits for offset
    ttl = 64           # 1 byte set 64
    proto = 6          # 1 byte set to 6(TCP)
    head_check = 0              # checksum placeholder
    source_ip = struct.unpack('!L', socket.inet_aton(my_ip))[0]           # 4 bytes 
    dest_ip = struct.unpack('!L', socket.inet_aton(target_ip))[0]               # 4 bytes

    ###################################
    # TCP packet field structutur
    ###################################

    s_port = random.randint(1025, 65536) # 2 bytes H
    d_port = target_port # 2 bytes H 
    seq_num = 1    # 4 bytes L
    ack = 0  # 4 bytes L
    len_flags = flag_value # 2 bytes (4/6/0/0/0/0/0/0 glags bits) H
    win_s = 8192 # 2 bytes H
    tcp_check = 0 # Placeholder 2 bytes H
    urg_p = 0 # 2 bytes H


    ###################################
    # Crafting Temp packets
    ###################################

    temp_ip_header = struct.pack('!BBHHHBBHLL', ver_ihl, serv_type, tot_l, id_pack, flag_frag, ttl, proto, head_check,source_ip, dest_ip)
    temp_tcp_header = struct.pack('!HHLLHHHH', s_port, d_port, seq_num,ack, len_flags, win_s, tcp_check, urg_p )


    ###################################
    # Calculate IP checksum and craft the final version of IP header
    ###################################

    head_check= calculate_check(temp_ip_header)
    tot_l = 40
    ip_header = struct.pack('!BBHHHBBHLL', ver_ihl, serv_type, tot_l, id_pack, flag_frag, ttl, proto, head_check,source_ip, dest_ip)

    ###################################
    # Calculate TCP checksum and craft the final version of IP header
    ###################################

    pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(my_ip), socket.inet_aton(target_ip), 0, socket.IPPROTO_TCP, len(temp_tcp_header))
    checksum_data = pseudo_header + temp_tcp_header

    tcp_check = calculate_check(checksum_data)

    tcp_header = struct.pack('!HHLLHHHH', s_port, d_port, seq_num,ack, len_flags, win_s, tcp_check, urg_p )

    ###################################
    # Craft the final TCP packet
    ###################################

    probe_pack = ip_header + tcp_header

    return probe_pack
