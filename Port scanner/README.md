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
### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```
2️⃣ Run the Script
```
python port_scanner.py
```

3️⃣ Enter Target IP
Example:
```
Enter the target IP address: 192.168.1.1
The program will scan ports from 1 to 1023 by default.
```
🧪 Example Output
```
Enter the target IP address: 192.168.1.1
Port 22 is open on 192.168.1.1
Port 80 is open on 192.168.1.1
Port 443 is open on 192.168.1.1
Open ports on 192.168.1.1: [22, 80, 443]
```

📌 Notes
Default port range: 1–1023
Threads: 500 by default for faster scanning
Can be modified for other port ranges or thread counts

💡 Enhancements (Future Ideas)
Allow custom port ranges via user input
Save scan results to a file
Add service detection for common ports
Add banner grabbing (fetch server info)
Use command-line arguments (argparse)

🔒 Ethical Use Reminder
❗ Port scanning without explicit permission may be illegal and is considered unethical. Use this tool only on networks you own or have authorization to scan.

📄 License
MIT License – For educational purposes only.

🤝 Contributing
Contributions are welcome! Feel free to fork, modify, and submit pull requests.

📧 Contact
For educational discussions, reach out at:
merwinofficial24@gmail.com


Let me know if you'd like a proper folder structure or setup instructions for a GitHub repository. I c
