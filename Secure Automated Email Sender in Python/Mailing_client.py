import os
import base64
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import datetime
from getpass import getpass

# ---------------- CONFIGURATION ----------------
ENC_KEY_FILE = 'key.enc'
PASSWORD_FILE = 'password.txt'
SALT_FILE = 'salt.bin'
PASSPHRASE_STORE = 'passphrase_store.txt'
OWNER_EMAIL = input("Enter your TO e-mail address: ")
ALERT_EMAIL = 'merwinking369@gmail.com'
BODY_FILE = 'body.txt'
IMG_ATTACHMENT = 'M.png'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# ---------------- SECURITY FUNCTIONS ----------------
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def encrypt_fernet_key(fernet_key: bytes, passphrase: str) -> None:
    salt = os.urandom(16)
    aesgcm = AESGCM(derive_key(passphrase, salt))
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, fernet_key, None)

    with open(ENC_KEY_FILE, 'wb') as f:
        f.write(nonce + encrypted)
    with open(SALT_FILE, 'wb') as f:
        f.write(salt)
    with open(PASSPHRASE_STORE, 'w') as f:
        f.write(passphrase)  # Automate future use

def decrypt_fernet_key(passphrase: str) -> bytes:
    with open(SALT_FILE, 'rb') as f:
        salt = f.read()
    aesgcm = AESGCM(derive_key(passphrase, salt))
    with open(ENC_KEY_FILE, 'rb') as f:
        data = f.read()
        nonce = data[:12]
        encrypted_key = data[12:]
        return aesgcm.decrypt(nonce, encrypted_key, None)

# ---------------- EMAIL ALERT ----------------
def send_alert_email(subject, body):
    try:
        fernet = Fernet(fernet_key)
        with open(PASSWORD_FILE, 'rb') as pf:
            password = fernet.decrypt(pf.read()).decode()
    except Exception:
        print("❌ Cannot decrypt password.")
        return

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(ALERT_EMAIL, password)

        msg = MIMEMultipart()
        msg['From'] = 'Alert System'
        msg['To'] = OWNER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(ALERT_EMAIL, OWNER_EMAIL, msg.as_string())
        server.quit()
        print("📧 Alert email sent to owner.")

    except Exception as e:
        print(f"❌ Email send failed: {e}")

# ---------------- KEY SETUP ----------------
if not os.path.exists(ENC_KEY_FILE):
    print("🔐 First-time setup: generating and encrypting key...")
    key = Fernet.generate_key()
    passphrase = getpass("Set a secure passphrase (for one-time setup): ")
    encrypt_fernet_key(key, passphrase)
    print("✅ Key saved securely.")

    with open(PASSWORD_FILE, 'rb') as pf:
        raw_pass = pf.read()
    f = Fernet(key)
    with open(PASSWORD_FILE, 'wb') as pf:
        pf.write(f.encrypt(raw_pass))
    print("🔐 Gmail password encrypted and saved.")
else:
    # Automatic passphrase retrieval
    try:
        with open(PASSPHRASE_STORE, 'r') as f:
            stored_passphrase = f.read().strip()
        fernet_key = decrypt_fernet_key(stored_passphrase)
        f = Fernet(fernet_key)
    except Exception:
        print("❌ Unauthorized Access Detected!")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_alert_email(
            subject="❗ Unauthorized Access Attempt Detected",
            body=f"Someone tried to access `key.enc` at {current_time} with an invalid passphrase."
        )
        exit(1)

# ---------------- SEND EMAIL ----------------
try:
    with open(PASSWORD_FILE, 'rb') as pf:
        decrypted_password = f.decrypt(pf.read()).decode()

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(ALERT_EMAIL, decrypted_password)

    msg = MIMEMultipart()
    msg['From'] = input("Enter your Name: ")
    msg['To'] = OWNER_EMAIL
    msg['Subject'] = input("Enter your Subject: ")

    if not os.path.exists(BODY_FILE):
        with open(BODY_FILE, 'w') as file:
            file.write("This is a test email body.")
        print("✅ Body file created. Please edit it before sending.")
    
    with open(BODY_FILE, 'r') as file:
        message = file.read()
        print(f"📜 Current message:\n{message}")
    
    choice = input("\n✏️ Do you want to edit the body? (y/n): ").strip().lower()

    if choice == 'y':
        print("\nEnter your new message (end with a single line containing only 'END'):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        message = "\n".join(lines)
        with open(BODY_FILE, 'w') as file:
            file.write(message)
            print(f"📝 '{BODY_FILE}' updated.")
    else:
        message = message

    msg.attach(MIMEText(message, 'plain'))

    with open(IMG_ATTACHMENT, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={IMG_ATTACHMENT}')
    msg.attach(part)

    server.sendmail(ALERT_EMAIL, OWNER_EMAIL, msg.as_string())
    server.quit()
    print("✅ Secure email sent successfully!")

except Exception as e:
    print(f"❌ Email sending failed: {e}")


