import hashlib
import secrets
import json
import os

USERS_FILE = 'users.json'

def sha3_256(data):
    return hashlib.sha3_256(data.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def register_user():
    username = input("👤 Enter new username: ").strip()
    secret = input("🔐 Enter your secret (like a password): ").strip()

    nonce = secrets.token_hex(16)  # 128-bit nonce
    commitment = sha3_256(secret + nonce)

    users = load_users()

    if username in users:
        print("⚠️ Username already exists. Try again.")
        return

    users[username] = {
        "commitment": commitment,
        "nonce": nonce
    }

    save_users(users)
    print(f"✅ User '{username}' registered successfully.")
    print(f"🧪 Stored Commitment: {commitment}")
    print(f"📌 Nonce (keep it safe): {nonce}")

if __name__ == "__main__":
    register_user()
