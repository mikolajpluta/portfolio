import math
import random
from tests import single_bit_test, long_serie_test, series_test, poker_test

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_nums_generator():
    number = random.randint(10000, 99999)
    while True:
        if is_prime(number) and number % 4 == 3:
            return number
        number += 1

def generate_x(N):
    x = random.randint(10000, 99999)
    while True:
        if math.gcd(N, x) == 1:
            return x
        x += 1

def generate_random_bits(n, N):
    result = ''
    for _ in range(n):
        x = x = generate_x(N)
        result += str(pow(x, 2, N) & 1)
    return result

def generate_random_bits2(n, N, x):
    result = ''
    last_x = x
    for _ in range(n):
        new_x = pow(last_x, 2, N)
        result += str(new_x & 1)
        last_x = new_x
    return result



q = prime_nums_generator()
p = prime_nums_generator()
N = p * q
x0 = generate_x(N)

print(q, p, N)

# data = generate_random_bits(20000, N)
data = generate_random_bits2(20000, N, x0)

print(data)
print(single_bit_test(data))
print(long_serie_test(data))
print(series_test(data))
print(poker_test(data))