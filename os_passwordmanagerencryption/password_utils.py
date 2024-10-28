# password_utils.py

import os
import base64
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Function to generate a random password
def generate_password(length=12):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Function to encrypt a password
def encrypt_password(password, key):
    # Generate a random 16-byte IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_password = iv + encryptor.update(password.encode()) + encryptor.finalize()
    return base64.b64encode(encrypted_password).decode()

# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    encrypted_password_bytes = base64.b64decode(encrypted_password)
    iv = encrypted_password_bytes[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_password = decryptor.update(encrypted_password_bytes[16:]) + decryptor.finalize()
    return decrypted_password.decode()
