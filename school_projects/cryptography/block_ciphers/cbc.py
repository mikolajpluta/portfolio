from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_random_bytes(size):
    return os.urandom(size)

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def encrypt_cbc(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = b""
    previous_block = iv
    for i in range(0, len(plaintext), 16):  
        block = plaintext[i:i+16]
        block_xor = xor_bytes(block, previous_block)
        encrypted_block = encryptor.update(block_xor)
        ciphertext += encrypted_block
        previous_block = encrypted_block
    return ciphertext + encryptor.finalize()

def decrypt_cbc(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = b""
    previous_block = iv
    for i in range(0, len(ciphertext), 16):  
        block = ciphertext[i:i+16]
        decrypted_block = decryptor.update(block)
        decrypted_block_xor = xor_bytes(decrypted_block, previous_block)
        plaintext += decrypted_block_xor
        previous_block = block
    return plaintext


key = generate_random_bytes(32)  
iv = generate_random_bytes(16)   
plaintext = b"Sample plaintext to be encrypted using CBC mode."


ciphertext = encrypt_cbc(key, iv, plaintext)
print("Ciphertext (CBC mode):", ciphertext)

decrypted_plaintext = decrypt_cbc(key, iv, ciphertext)
print("Decrypted plaintext (CBC mode):", decrypted_plaintext)
