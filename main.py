#!/usr/bin/env python3

import base64
from crypto import encrypt, decrypt
from lib import checkPaddingLength

# Message to encrypt
message = "This is a secret message."

# Encryption parameters
iv = '123456789abcdef5'
key = 'abcjdnfmksiutlkj'

# Encrypt message
encrypted_message = encrypt(message.encode(), iv, key)

# Print encrypted message
print(f"Encrypted message: {encrypted_message}")

# Decrypt message
decrypted_message = decrypt(base64.b64decode(encrypted_message), iv, key)

# Print decrypted message
print(f"Decrypted message: {decrypted_message.decode()}")

# Padding oracle attack
checkPaddingLength(base64.b64decode(encrypted_message), iv, key)
