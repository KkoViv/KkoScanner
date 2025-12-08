###################################
# NEEDED MODULES
###################################

import struct
from netlib.calculate_check import calculate_check

###################################
# Craft the ICMP packet
###################################

def ICMP_Creation(data):

    # current version of function receives sys.argv as data, but without handle it
    
    ICMP_Type = 8    # 0000 1000
    ICMP_Code = 0    # 0000 0000
    checksum = 0     # this is just a pinpoint bc we need to add the checksum after calculating his value based on the entire icmp
    ID_entifier = 1234 # just a random number
    sequence = 0
    D_ata = "CiaoPing" 
    payload = D_ata.encode()

    temp_header = struct.pack("!BBHHH", ICMP_Type, ICMP_Code, checksum, ID_entifier, sequence) # create the header of ICMP in Bytes

    pack_x_check = temp_header + payload  # add the payload in bytes

    checksum = calculate_check(pack_x_check)# call the checksum() function

    official_header= struct.pack("!BBHHH", ICMP_Type, ICMP_Code, checksum, ID_entifier, sequence) # add the checksum to the ICMP header

    ICMP_Pack = official_header + payload  # add the payload to the ICMP header.

    return ICMP_Pack