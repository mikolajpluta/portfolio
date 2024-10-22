import random
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_num_generator():
    number = random.randint(1000, 9999)
    while True:
        if is_prime(number):
            return number
        number += 1

def relatively_prime(x):
    y = prime_num_generator()
    while math.gcd(y, x) != 1:
        y = prime_num_generator()
    return y

def generate_d(e ,phi):
    d = random.randint(99999, 999999)
    if e*d-1 >= phi:
        d = random.randint(99999, 999999)

    while not (e*d-1) % phi == 0:
        d += 1
    return d

def encript(e, n, msg):
    encrypted = []
    for char in msg:
        encrypted.append(pow(ord(char), e, n))
    return encrypted

def decript(d, n, msg):
    decripted = ''
    for char in msg:
        decripted += chr(pow(char, d, n))
    return decripted

p = prime_num_generator()
q = prime_num_generator()

n = p * q
phi = (p-1)*(q-1)
e = relatively_prime(phi)
d = generate_d(e, phi)

message = "Ala ma kota, a kot ma Ale. Kot Ali mruczy, gdy Al."
encrypted = encript(e, n , message)
decripted = decript(d, n, encrypted)

print(phi)
print(e)
print(d)
print(encrypted)
print(decripted)



