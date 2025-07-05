# MITMProxy Proxy Server with GUI, URL Logging, and Domain Blacklisting

A Python-based proxy tool powered by `mitmproxy` with the following key features:

- Logs every visited URL with user IP and timestamp
- Alerts when users visit blacklisted domains
- Simple Tkinter GUI to control the proxy
- Works on local network IPs (not limited to 127.0.0.1)
- Stores logs in JSON format for analysis

---

## 🗂️ Directory Structure
```
├── logger_addon.py         # Handles URL logging, alerts, and blacklist
├── gui_viewer.py           # GUI to view logs & alerts
├── run_gui.py              # Launches the GUI
├── cert_installer.py       # Installs mitmproxy certificate
├── traffic_simulator.py    # Optional: sends fake requests to test
├── logs.json               # Log file (auto-created)
├── alerts.log              # Alert log file (auto-created)
```

## 📦 Requirements

Python 3.8 or above

Install dependencies:
✅ 1. Run mitmproxy with Custom Addon
```
mitmproxy -s logger_addon.py --listen-port 8085 --listen-host 0.0.0.0
```
➡️This makes the proxy listen on all IP addresses, not just 127.0.0.1.

✅ 2. Run GUI in another terminal
```
python run_gui.py
```
✅ 3. (Optional) Install Certificate
```
python cert_installer.py
```
➡️ This ensures HTTPS sites don’t throw ERR_CERT_AUTHORITY_INVALID.

✅ 4. Configure Browser Proxy
Set your browser/system proxy to:
```
Host: localhost your ip address (ipconfig in cmd)
Port: 8085
```
Now visit some sites (like YouTube) to trigger alerts.

🛑 Common Errors & Fixes
Error [WinError 10013]:
Run script as administrator
Or change port to >1024 (e.g., 8085)
Error ERR_CERT_AUTHORITY_INVALID or HSTS errors:
Install mitmproxy certificate in browser/system
Some HSTS domains (e.g., Google) cannot be intercepted

🔒 Disclaimer
This tool is for educational and authorized use only. Do not deploy it in production or public networks without proper legal and ethical authorization.

🧑‍💻 Author
Created by: Merwin J
© 2025 | CyberSecurity-Projects
