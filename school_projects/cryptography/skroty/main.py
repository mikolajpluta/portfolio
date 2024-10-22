import hashlib
import time

input_string = input("Podaj tekst do wygenerowania skrótów: ")

start_time = time.perf_counter()
md5_hash = hashlib.md5(input_string.encode()).hexdigest()
md5_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
sha1_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha224_hash = hashlib.sha224(input_string.encode()).hexdigest()
sha224_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
sha256_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha384_hash = hashlib.sha384(input_string.encode()).hexdigest()
sha384_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha512_hash = hashlib.sha512(input_string.encode()).hexdigest()
sha512_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha3_224_hash = hashlib.sha3_224(input_string.encode()).hexdigest()
sha3_224_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha3_256_hash = hashlib.sha3_256(input_string.encode()).hexdigest()
sha3_256_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha3_384_hash = hashlib.sha3_384(input_string.encode()).hexdigest()
sha3_384_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
sha3_512_hash = hashlib.sha3_512(input_string.encode()).hexdigest()
sha3_512_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
shake128_hash = hashlib.shake_128(input_string.encode()).hexdigest(224) # 224 bit skrót
shake128_time = (time.perf_counter() - start_time) * 1_000_000

start_time = time.perf_counter()
shake256_hash = hashlib.shake_256(input_string.encode()).hexdigest(256) # 256 bit skrót
shake256_time = (time.perf_counter() - start_time) * 1_000_000

print("\nMD5:\nHash:", md5_hash, "\nCzas wykonania:", "{:.4f}".format(md5_time), "µs")
print("\nSHA-1:\nHash:", sha1_hash, "\nCzas wykonania:", "{:.4f}".format(sha1_time), "µs")

print("\nZ GRUPY SHA-2")
print("SHA-224:\nHash:", sha224_hash, "\nCzas wykonania:", "{:.4f}".format(sha224_time), "µs")
print("SHA-256:\nHash:", sha256_hash, "\nCzas wykonania:", "{:.4f}".format(sha256_time), "µs")
print("SHA-384:\nHash:", sha384_hash, "\nCzas wykonania:", "{:.4f}".format(sha384_time), "µs")
print("SHA-512:\nHash:", sha512_hash, "\nCzas wykonania:", "{:.4f}".format(sha512_time), "µs")

print("\nZ GRUPY SHA-3")
print("SHA3-224:\nHash:", sha3_224_hash, "\nCzas wykonania:", "{:.4f}".format(sha3_224_time), "µs")
print("SHA3-256:\nHash:", sha3_256_hash, "\nCzas wykonania:", "{:.4f}".format(sha3_256_time), "µs")
print("SHA3-384:\nHash:", sha3_384_hash, "\nCzas wykonania:", "{:.4f}".format(sha3_384_time), "µs")
print("SHA3-512:\nHash:", sha3_512_hash, "\nCzas wykonania:", "{:.4f}".format(sha3_512_time), "µs")
print("SHAKE128 (224 bit):\nHash:", shake128_hash, "\nCzas wykonania:", "{:.4f}".format(shake128_time), "µs")
print("SHAKE256 (256 bit):\nHash:", shake256_hash, "\nCzas wykonania:", "{:.4f}".format(shake256_time), "µs")
