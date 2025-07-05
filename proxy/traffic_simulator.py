import requests

proxies = {
    "http": "http://localhost:8085",
    "https": "http://localhost:8085"
}

print("[*] Sending test requests...")
urls = [
    "http://example.com",
    "https://www.google.com",
    "https://www.youtube.com"
]

for url in urls:
    try:
        res = requests.get(url, proxies=proxies, verify=False)
        print(f"[+] {url} => {res.status_code}")
    except Exception as e:
        print(f"[!] {url} failed: {e}")
