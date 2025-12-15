# this file defines the class to store info about scan parameters, statistics and data
import threading

class ScanParam:
    def __init__(self):

# Scan paramenters

        self.target_ip = None                           
        self.port_info = None
        self.port_list = []         # filled by user port choice
        self.type_scan = None       # for now open/half open scan
        self.my_ip = None
        self.scan_list = []         # list of port generated from port_list
        self.sorted_dict = {}       # dictionary that store the scanning result / port as key
        self.semaphore = threading.Semaphore(1000)      # generale semaphore 

# Statistic parameters

        self.recv_pack_errors = 0       
        self.malformed_pack = 0
        self.short_pack = 0
        self.socket_created = 0
        self.packet_created = 0
        self.pack_sent = 0

# Errors parameters

        self.error_response = {}        # filled by failed sending packet
        self.socket_creation_e = 0      # error during socket creation
        self.packet_creation_e = 0      # error during packet creation
        self.sending_error = 0          # error during the delivery of packet
        self.thresold_error = 10 # 10% E.g: socket_creation_e / (socket_created + socket_creation_e) - the scan is compromise

        #Python hashtag#Debugging hashtag#SoftwareEngineering hashtag#Coding hashtag#LogicError