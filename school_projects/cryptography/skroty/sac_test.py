import hashlib
import random

# Testowany algorytm skrotu (SHA-256)
hash_func = hashlib.sha256

input_data = b"Test input data"

original_hash = hash_func(input_data).digest()
original_hash_bin = ''.join(format(byte, '08b') for byte in original_hash)

input_bits = len(input_data) * 8

for i in range(input_bits):
    changed_bits_count = 0
    modified_input = bytearray(input_data)

    modified_input[i // 8] ^= (1 << (7 - i % 8))

    modified_hash = hash_func(modified_input).digest()
    modified_hash_bin = ''.join(format(byte, '08b') for byte in modified_hash)
    for j in range(len(original_hash_bin)):
        if original_hash_bin[j] != modified_hash_bin[j]:
            changed_bits_count += 1

    print("liczba bitow skrtotu:", len(original_hash_bin))
    print("Ilość zmienionych bitów:", changed_bits_count)
