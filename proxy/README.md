# MITMProxy Proxy Server with GUI, URL Logging, and Domain Blacklisting

A Python-based proxy tool powered by `mitmproxy` with the following key features:

- Logs every visited URL with user IP and timestamp
- Alerts when users visit blacklisted domains
- Simple Tkinter GUI to control the proxy
- Works on local network IPs (not limited to 127.0.0.1)
- Stores logs in JSON format for analysis

---

## 🗂️ Directory Structure

.
├── main.py                   # GUI interface to start proxy
├── proxy_interceptor.py     # MITMProxy add-on (core logic)
├── requirements.txt          # Python dependencies
├── logs/
│   └── log.json              # URL logs
├── alerts/
│   └── alerts.log            # Alert log
└── README.md

---

## 📦 Requirements

Python 3.8 or above

Install dependencies:

```bash
pip install -r requirements.txt
requirements.txt:

text
Copy
Edit
mitmproxy
tk
🔐 Setup HTTPS Interception
Run mitmproxy once to generate certificates:

bash
Copy
Edit
mitmproxy
Visit in browser:
http://mitm.it

Download and install the certificate for your OS/browser.

For Firefox:

Go to Settings → Privacy & Security → View Certificates → Import

🚀 Running the Proxy GUI
Run this command:

bash
Copy
Edit
python main.py
GUI will appear with a Start Proxy button.

Starts the proxy on 0.0.0.0:8085

Configure your browser or device to use the proxy IP:

Example: 192.168.1.5:8085

⚠️ Domain Blacklist
Modify the blacklist in proxy_interceptor.py:

python
Copy
Edit
blacklist = ["www.youtube.com", "www.tiktok.com", "www.instagram.com"]
📄 Log Format (logs/log.json)
json
Copy
Edit
[
  {
    "user_ip": "192.168.1.10",
    "url": "https://www.example.com",
    "timestamp": "2025-07-05 17:22:10"
  }
]
🚨 Alert Format (alerts/alerts.log)
pgsql
Copy
Edit
[ALERT] 2025-07-05 17:23:01 - 192.168.1.10 tried to access blacklisted domain: www.youtube.com
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
Created by: [Your Name]
© 2025 | CyberSecurity-Projects

yaml
Copy
Edit

---

Let me know if you’d like a downloadable `.md` file or a ZIP with the whole project structure includ
