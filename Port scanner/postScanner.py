import socket
import threading
from queue import Queue

target= input("Enter the target IP address: ")
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            open_ports.append(port)
            print(f"Port {port} is open on {target}")

port_list = range(1, 1024)  
fill_queue(port_list)

threads = []
for _ in range(500): 
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Open ports on {target}: {open_ports}")