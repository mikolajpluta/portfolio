import random

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

def is_primary_root(g, n):
    lst = []
    for i in range(1, n):
        x = pow(g, i, n)
        if x in lst:
            return False
        lst.append(x)
    return True

def generate_g(n):
    g = 2
    while not is_primary_root(g, n):
        g += 1
    if g >= n:
        print("nie znalezniono pierwiastka pierwotnego dla tej wartości")
        return None
    else:
        return g

#wspolne
n = prime_num_generator()
g = generate_g(n)

# A wybiera
x = random.randint(1000, 9999)
X = pow(g, x, n)

# B wybiera
y = random.randint(1000, 9999)
Y = pow(g, y, n)

kA = pow(Y, x, n)
kB = pow(X, y, n)

print(kA)
print(kB)