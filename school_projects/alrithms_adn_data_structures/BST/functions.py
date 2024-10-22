import random
# funkcja do zaokraglania floatow
def rnd(x,n):
    multipler=10**n
    x=x*multipler
    x=round(x)
    return x/multipler
#generator listy n losowych elementow z zakresu <1,10*n>
def generate_random(n):
    l=[]
    for i in range(n):
        l.append(random.randint(1,10*n))
    return l

#generator listy n rosnacych elementow z zakresu <1,10*n>
def generate_rise(n):
    l=[]
    for i in range(n):
        x=10*i+1
        l.append(random.randint(x,x+10))
    return l

#generator listy n malejących elementow z zakresu <1,10*n>
def generate_decrease(n):
    l=[]
    for i in range(n):
        x=10*i+1
        l.append(random.randint(x,x+10))
    return l[::-1]
l=generate_decrease(10)

#generowanie listy A ksztaltnej n elementowej z zakresu<1,10*n>
def generate_Ashape(n):
    x=n//2
    l=generate_rise(x) + generate_decrease(n-x)
    return l

#generowanie listy V ksztaltnej n elementowej z zakresu<1,10*n>
def generate_Vshape(n):
    x=n//2
    l=generate_decrease(n-x) + generate_rise(x)
    return l

