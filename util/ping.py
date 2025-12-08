# this file perform a ping

from netlib.icmp_creation import ICMP_Creation
from netlib.sent_icmp import sent_icmp

###################################
# CORE FUNCTION
###################################

def ping(target_ip):

    icmp_packet = ICMP_Creation(target_ip)                 # create a ICMP message as a variable
    
    result_of_ping = sent_icmp(target_ip, icmp_packet)                              # perform the ping

    return result_of_ping