from mitmproxy import http
import json
import datetime

BLACKLIST = {"www.youtube.com", "www.reddit.com"}
LOG_FILE = "logs.json"
ALERT_FILE = "alerts.log"

class LoggerAddon:
    def __init__(self):
        self.visits = []

    def request(self, flow: http.HTTPFlow):
        user_ip = flow.client_conn.peername[0]
        timestamp = datetime.datetime.now().isoformat()
        url = flow.request.pretty_url

        log_entry = {
            "ip": user_ip,
            "time": timestamp,
            "url": url
        }

        # Save to logs
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        # Blacklist check
        for blocked in BLACKLIST:
            if blocked in url:
                with open(ALERT_FILE, "a") as alert_file:
                    alert_file.write(f"[ALERT] {user_ip} tried to access blacklisted domain: {url}\n")
                flow.response = http.Response.make(
                    403,  # Forbidden
                    b"Blocked by proxy policy",
                    {"Content-Type": "text/html"}
                )
                return

addons = [LoggerAddon()]
