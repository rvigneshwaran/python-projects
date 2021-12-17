from io import open_code
from socket import *
import time

if __name__ == "__main__":
    startTime = time.time
    host_ip_adddress = input("Enter the Host to be Scanned for Ports :: ")
    target_ip = gethostbyname(host_ip_adddress)
    print("Start Scanning for the Host :: ",host_ip_adddress)
    
    post_scanner = {}
    open_ports = []
    closed_ports = []
    for index_port in range(50,500):
        socket_instance = socket(AF_INET,SOCK_STREAM)
        connection_res = socket_instance.connect_ex((target_ip,index_port))
        if connection_res == 0:
            print("Post %d :: Open "%(index_port,))
            open_ports.append(index_port)
        else:
            closed_ports.append(index_port)
        socket_instance.close()
    print('Time taken :', str(time.time() - startTime))
    post_scanner["Open_ports"] = open_ports
    post_scanner["closed-ports"] = closed_ports
    post_scanner["host-scanned"] = target_ip
    print("Port Scanner output :: "+str(post_scanner))

