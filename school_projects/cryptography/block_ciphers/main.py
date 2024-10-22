from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import time
import matplotlib.pyplot as plt

def generate_random_bytes(size):
    return os.urandom(size)

# Measure encryption and decryption time for different data sizes and modes
data_sizes = [10, 100, 1000]  # Specify different file sizes in megabytes
key_size = 32
iv_size = 16
nonce_size = 16

# Lists to store encryption and decryption times for each mode
ecb_encrypt_times = []
ecb_decrypt_times = []
cbc_encrypt_times = []
cbc_decrypt_times = []
ctr_encrypt_times = []
ctr_decrypt_times = []

for size in data_sizes:
    data = generate_random_bytes(size * 1024 * 1024)
    key = generate_random_bytes(key_size)
    iv = generate_random_bytes(iv_size)
    nonce = generate_random_bytes(nonce_size)

    # ECB Mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    # ECB Mode Encryption
    encryptor = cipher.encryptor()
    start_time = time.time()
    ciphertext_ecb = encryptor.update(data) + encryptor.finalize()
    ecb_encrypt_time = time.time() - start_time
    ecb_encrypt_times.append(ecb_encrypt_time)

    # ECB Mode Decryption
    decryptor = cipher.decryptor()
    start_time = time.time()
    decrypted_ecb = decryptor.update(ciphertext_ecb) + decryptor.finalize()
    ecb_decrypt_time = time.time() - start_time
    ecb_decrypt_times.append(ecb_decrypt_time)

    # CBC Mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # CBC Mode Encryption
    encryptor = cipher.encryptor()
    start_time = time.time()
    ciphertext_cbc = encryptor.update(data) + encryptor.finalize()
    cbc_encrypt_time = time.time() - start_time
    cbc_encrypt_times.append(cbc_encrypt_time)

    # CBC Mode Decryption
    decryptor = cipher.decryptor()
    start_time = time.time()
    decrypted_cbc = decryptor.update(ciphertext_cbc) + decryptor.finalize()
    cbc_decrypt_time = time.time() - start_time
    cbc_decrypt_times.append(cbc_decrypt_time)

    # CTR Mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())

    # CTR Mode Encryption
    encryptor = cipher.encryptor()
    start_time = time.time()
    ciphertext_ctr = encryptor.update(data) + encryptor.finalize()
    ctr_encrypt_time = time.time() - start_time
    ctr_encrypt_times.append(ctr_encrypt_time)

    # CTR Mode Decryption
    decryptor = cipher.decryptor()
    start_time = time.time()
    decrypted_ctr = decryptor.update(ciphertext_ctr) + decryptor.finalize()
    ctr_decrypt_time = time.time() - start_time
    ctr_decrypt_times.append(ctr_decrypt_time)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(data_sizes, ecb_encrypt_times, marker='o', label='ECB Encryption Time')
plt.plot(data_sizes, ecb_decrypt_times, marker='o', label='ECB Decryption Time')
plt.plot(data_sizes, cbc_encrypt_times, marker='o', label='CBC Encryption Time')
plt.plot(data_sizes, cbc_decrypt_times, marker='o', label='CBC Decryption Time')
plt.plot(data_sizes, ctr_encrypt_times, marker='o', label='CTR Encryption Time')
plt.plot(data_sizes, ctr_decrypt_times, marker='o', label='CTR Decryption Time')

plt.title('Encryption and Decryption Time vs Data Size')
plt.xlabel('Data Size (MB)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)

# Saving the plot
plt.savefig('encryption_decryption_times_plot.png')

plt.show()
