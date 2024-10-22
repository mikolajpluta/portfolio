from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_random_bytes(size):
    return os.urandom(size)

def inject_error(data):
    # Injecting error by flipping the second bit of the first byte
    data_with_error = bytearray(data)
    data_with_error[0] ^= 0b00000010
    return bytes(data_with_error)

# Generating key and initialization vector
key = generate_random_bytes(32)
iv = generate_random_bytes(16)

# Plaintext to be encrypted and decrypted
plaintext = b"To jest przykladowy tekst, ktorego szyfrogram ma zmieniony drugi bit pierwszego bajtu"
print("tekst do zaszyfrowania:\n", plaintext)

# Padding plaintext to match block size
block_size = 16  # AES block size in bytes
remainder = len(plaintext) % block_size
if remainder:
    padding_length = block_size - remainder
    plaintext += bytes([padding_length]) * padding_length

# Encrypting with error
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
ciphertext_with_error = inject_error(ciphertext)  # Introducing error to the ciphertext

print("zaszyfrowany tekst:\n\n", ciphertext)
print("\n\nzaszyfrowany tekst po wprowadzeniu bledu:\n\n", ciphertext_with_error)

# Decrypting with error
decryptor = cipher.decryptor()
plaintext_with_error = decryptor.update(ciphertext_with_error) + decryptor.finalize()
plaintext_with_error = inject_error(plaintext_with_error)  # Introducing error to the decrypted plaintext

print("rozszyfrowany tekst:\n", plaintext_with_error)
