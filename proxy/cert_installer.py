import os
import shutil
import subprocess

print("[*] Generating and installing mitmproxy CA cert...")

mitmproxy_dir = os.path.expanduser("~/.mitmproxy")
cert_file = os.path.join(mitmproxy_dir, "mitmproxy-ca-cert.pem")

# Ensure mitmproxy ran at least once to generate cert
if not os.path.exists(cert_file):
    print("[!] Run `mitmproxy` once first to generate cert.")
    exit(1)

# Windows: Add to trusted root store
try:
    subprocess.run(["certutil", "-addstore", "Root", cert_file], check=True)
    print("[+] Certificate installed successfully.")
except Exception as e:
    print(f"[!] Error installing certificate: {e}")
