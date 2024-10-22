import hashlib
import random

bits_to_compare = 12

hashed_messages = {}

messages_generated = 0

try:
    while True:
        message = str(random.getrandbits(32))
        
        sha256_hash = hashlib.sha256(message.encode()).digest()
        
        first_bits = sha256_hash[:bits_to_compare // 8]
        first_bits_bin = ''.join(format(byte, '08b') for byte in first_bits)
        
        if first_bits_bin in hashed_messages:
            print("Kolizja na pierwszych {} bitach:".format(bits_to_compare))
            print("Wiadomość:", message)
            print("Poprzednie skróty dla tej samej sekwencji bitów:")
            for previous_message, previous_hash in hashed_messages[first_bits_bin]:
                print("- Wiadomość:", previous_message)
                print("- Skrót:", previous_hash.hex())
            break
        
        if first_bits_bin not in hashed_messages:
            hashed_messages[first_bits_bin] = [(message, sha256_hash)]
        
        messages_generated += 1

except KeyboardInterrupt:
    print("\n\nPrzerwano program.\nWygenerowano {} wiadomości.".format(messages_generated))
