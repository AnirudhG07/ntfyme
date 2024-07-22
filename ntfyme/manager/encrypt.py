import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(password: str, key: str) -> str:
    # Generate a random salt
    salt = os.urandom(16)

    # Derive a 32-byte encryption key from the provided key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    encryption_key = kdf.derive(key.encode())

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a Cipher object using the encryption key and IV
    cipher = Cipher(
        algorithms.AES(encryption_key), modes.CFB(iv), backend=default_backend()
    )
    encryptor = cipher.encryptor()

    # Encrypt the password
    encrypted_password = encryptor.update(password.encode()) + encryptor.finalize()

    # Encode the salt, IV, and encrypted password in base64 and concatenate them
    encoded_encrypted_password = base64.b64encode(
        salt + iv + encrypted_password
    ).decode("utf-8")

    return encoded_encrypted_password


def decrypt(encrypted_password: str, key: str) -> str:
    # Decode the base64 encoded string
    encrypted_password_bytes = base64.b64decode(encrypted_password)

    # Extract the salt, IV, and encrypted password
    salt = encrypted_password_bytes[:16]
    iv = encrypted_password_bytes[16:32]
    encrypted_password = encrypted_password_bytes[32:]

    # Derive the encryption key using the same parameters
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    encryption_key = kdf.derive(key.encode())

    # Create a Cipher object using the encryption key and IV
    cipher = Cipher(
        algorithms.AES(encryption_key), modes.CFB(iv), backend=default_backend()
    )
    decryptor = cipher.decryptor()

    # Decrypt the password
    decrypted_password = decryptor.update(encrypted_password) + decryptor.finalize()

    return decrypted_password.decode("utf-8")
