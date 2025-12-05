# this file calculate the checksum

###################################
# Calculate ate the checksum
###################################

def calculate_check(packet):                                # calculate the checksum of the TCP


    if (len(packet)%2) != 0:                                # IF length of packet is odd:
        packet = packet + b'\x00'                            #Add one null byte (0x00) at the end to make it even

    my_sum = 0                                              # Set Sum to 0

    for i in range(0, len(packet), 2):                      # FOR each 2 bytes in packet:
        word = (packet[i] << 8) + packet[i+1]                 # Combine them into one 16-bit integer (big endian)
        my_sum = my_sum + word                                      # Add that 16-bit number to Sum

    while my_sum > 0xFFFF:                                  # WHILE Sum > 0xFFFF:
        Carry = my_sum >> 16                                # extract bits beyond 16 bits
        my_sum = (my_sum & 0xFFFF) + Carry                  # pack the carry in my_sum

    my_sum = ~my_sum & 0xFFFF                               # Invert all bits in Sum (flip 0s to 1s and 1s to 0s)

    return my_sum