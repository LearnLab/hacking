#!/usr/bin/env python3

import base64
from Crypto.Cipher import AES

# Encrypt a message using AES with CBC mode
def encrypt(message, iv, key):
    binaryKey = bytes(key, "utf-8")
    binaryIV = bytes(iv, "utf-8")

    cipher = AES.new(binaryKey, AES.MODE_CBC, binaryIV)

    # Pad the message with PKCS7 padding
    padding_length = AES.block_size - len(message) % AES.block_size
    padded_message = message + bytes([padding_length]) * padding_length

    # Encrypt the message and return the base64 encoded ciphertext
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(ciphertext).decode()

# Decrypt a message using AES with CBC mode
def decrypt(ciphertext, iv, key):
    binaryKey = bytes(key, "utf-8")
    binaryIV = bytes(iv, "utf-8")

    cipher = AES.new(binaryKey, AES.MODE_CBC, binaryIV)

    # Decrypt the ciphertext and remove PKCS7 padding
    padded_message = cipher.decrypt(ciphertext)
    padding_length = padded_message[-1]
    message = padded_message[:-padding_length]

    return message
