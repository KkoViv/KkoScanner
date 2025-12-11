# this file defines the class to store info about scan parameters
import threading

class ScanParam:
    def __init__(self):
        self.target_ip = None                           
        self.port_info = None
        self.port_list = []
        self.type_scan = None
        self.my_ip = None
        self.scan_list = []
        self.sorted_dict = {}
        self.semaphore = threading.Semaphore(1000)
        self.recv_pack_errors = 0
        self.malformed_pack = 0
        self.short_pack = 0
        self.error_response = {}
