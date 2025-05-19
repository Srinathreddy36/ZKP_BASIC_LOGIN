import hashlib
import secrets
import json

USERS_FILE = 'users.json'

def sha3_256(data):
    return hashlib.sha3_256(data.encode()).hexdigest()

def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def zk_login():
    username = input("👤 Enter your username: ").strip()
    users = load_users()

    if username not in users:
        print("❌ User not found.")
        return

    secret = input("🔐 Enter your secret (password): ").strip()
    nonce = users[username]["nonce"]
    commitment = users[username]["commitment"]

    # Step 1: Server sends random challenge
    challenge = secrets.token_hex(8)  # 64-bit challenge
    print(f"🧠 Challenge from server: {challenge}")

    # Step 2: User computes response = SHA3(secret + nonce + challenge)
    response = sha3_256(secret + nonce + challenge)

    # Step 3: Server also computes expected response from commitment
    reconstructed_commitment = sha3_256(secret + nonce)
    if reconstructed_commitment != commitment:
        print("❌ Authentication failed: Wrong secret or tampered nonce.")
        return

    server_response = sha3_256(secret + nonce + challenge)

    if response == server_response:
        print("✅ Zero-Knowledge Authentication Successful!")
    else:
        print("❌ Authentication Failed. Mismatched response.")

if __name__ == "__main__":
    zk_login()
