# 🛡️ Multithreaded Port Scanner (Python)

> 🚨 **Disclaimer**: This tool is for educational and ethical purposes only. Do not use it for scanning unauthorized networks or devices. Unauthorized port scanning may violate laws and terms of service.

---

## 📌 Overview

This is a simple yet powerful **Multithreaded Port Scanner** built using Python. It allows you to scan a target IP address across a specified range of ports (default: 1-1023) to detect open ports.

Key features include:
- ✅ Fast scanning using multithreading (500 threads by default)
- ✅ Queue-based port management
- ✅ Easy to use via terminal prompts
- ✅ Clear output of detected open ports

---

## ⚙️ How It Works

1. **Input Target**: The user enters a target IP address (or domain name).
2. **Port Queue**: A queue is populated with the port range (default: 1–1023).
3. **Worker Threads**: Multiple threads scan the ports concurrently.
4. **Port Check**: Each thread tries to connect to a port. If successful, the port is open.
5. **Results**: Open ports are displayed and stored in a list.

---

## 🚀 Usage

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```
