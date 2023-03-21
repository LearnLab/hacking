#!/usr/bin/env python3

from crypto import decrypt

# Check the length of the padding for a ciphertext
def checkPaddingLength(ciphertext, iv, key):
    for i in range(1, 17):
        # Modify the last i bytes of the ciphertext
        modified_ciphertext = bytearray(ciphertext)
        for j in range(i):
            modified_ciphertext[-j-1] ^= i ^ (i+1)

            # Attempt to decrypt the modified ciphertext
            try:
                decrypt(modified_ciphertext, iv, key)
            except ValueError as e:
                # If the padding is invalid, print the padding length
                padding_length = int(str(e).split()[-1])
                print(f"Padding length: {padding_length}")
