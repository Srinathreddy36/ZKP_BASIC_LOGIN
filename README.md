Basic ZKP Authentication Login
Overview
This project demonstrates a Basic Zero-Knowledge Proof (ZKP) based Authentication Login system.
It showcases how a user (Prover) can prove knowledge of a secret (password or key) to a verifier (server) without revealing the secret itself, enhancing security and privacy during login.

The implementation is a simple simulation intended for educational purposes to illustrate ZKP concepts applied to authentication.

Features
Interactive Zero-Knowledge Proof protocol between Prover and Verifier

No password transmission over the network — only proof of knowledge

Basic CLI-based login simulation

Separate roles for Prover and Verifier in different scripts/modules

Easy to extend or integrate with real-world authentication systems

How It Works
Registration: The user sets a secret (password/key).

Login: Instead of sending the password, the user generates a cryptographic proof demonstrating knowledge of the secret.

Verification: The server verifies the proof without learning the secret.

Access Granted if verification is successful, else denied.

Getting Started
Prerequisites
Python 3.7 or above

Required libraries: (if any, e.g., pycryptodome, hashlib, etc.)
