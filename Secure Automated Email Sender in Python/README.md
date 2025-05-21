# 🔐 Secure Automated Email Sender in Python

This project is a **secure, automated email sender** built in Python. It encrypts your Gmail password using **Fernet + AES** with a **passphrase**, stores it securely, and decrypts it only at runtime for login—**no manual input required after setup**.

---

## 🚀 Features

- ✅ Encrypts and stores your Gmail password securely
- 🔐 AES encryption of `key.key` with a passphrase using `PyCryptodome`
- ✉️ Sends plain-text emails with optional file attachments
- 📄 Allows editable email body through a text file (`body.txt`)
- 🛡️ Safe for automation — no need to enter passphrase at runtime
- ⚙️ Automatically creates required files if they don’t exist

---

## 📁 Folder Structure

📦 secure-email-sender
├── send_email.py # Main script
├── password.txt # Encrypted password (generated)
├── key.enc # AES-encrypted Fernet key (generated)
├── body.txt # Email body (created if missing)
├── M.png # Optional attachment file
├── README.md # This file

yaml
Copy
Edit

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/secure-email-sender.git
cd secure-email-sender
2. Install Dependencies
bash
Copy
Edit
pip install cryptography pycryptodome
🔐 Setup (One-Time Only)
Run the script for the first time:

bash
Copy
Edit
python send_email.py
Enter your Gmail password when prompted. This will:

Encrypt and save the password in password.txt

Create a key.key (Fernet key)

Encrypt key.key using AES + a predefined passphrase

Store the AES-encrypted key as key.enc

⚠️ Important: Use App Passwords for Gmail if you have 2FA enabled.

📩 Sending an Email
After setup, just run:

bash
Copy
Edit
python send_email.py
It will:

Read your encrypted password securely

Allow you to edit the message body in the terminal or use the saved one

Send the email with an optional attachment (e.g., M.png)

🛠️ Customization
Change Sender or Receiver
Edit these lines in send_email.py:

python
Copy
Edit
EMAIL_ADDRESS = 'your_email@gmail.com'
TO_ADDRESS = 'receiver_email@gmail.com'
Change Attachment
Replace the file M.png or modify the ATTACHMENT variable.

🔐 How It Works
Fernet Encryption:

Your Gmail password is encrypted with a symmetric key.

AES Encryption of Fernet Key:

The symmetric key (key.key) is encrypted using AES-GCM with a passphrase.

Automation Friendly:

The passphrase is stored in the script (modify if you want interactive entry).

🧪 Example
bash
Copy
Edit
$ python send_email.py

✅ 'body.txt' created with default content.

📩 Default email body:
----------------------------------------
Hello,

This is the default email body.

Regards,
Your Automation System
----------------------------------------

✏️ Do you want to edit the body? (y/n): y
Enter your new message (end with a single line containing only 'END'):
Hey Team,
This is an automated email sent using our new Python tool.
Thanks!
END
📝 'body.txt' updated.
✅ Email sent successfully.
⚠️ Security Notes
Do not commit password.txt or key.enc to a public repository.

You may wish to encrypt the script or move credentials to a safer location.

For better security, consider using environment variables or vaults.

📜 License
MIT License. See LICENSE file.

👨‍💻 Author
Merwin J
If you found this useful, feel free to ⭐ the repo and connect with me on LinkedIn or GitHub!

yaml
Copy
Edit

---

### ✅ Next Steps:

- Save this content as `README.md` in your project directory.
- Update the GitHub repo link and username where applicable.
- Run this in your terminal to initialize your repo (if needed):

```bash
git init
git add .
git commit -m "Initial commit: secure email sender"
git remote add origin https://github.com/yourusername/secure-email-sender.git
git push -u origin main
