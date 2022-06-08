

def primeSieve(size):
    sieve = [True]*size
    sieve[0] = sieve[1] = False
    for i in range(2, int(size**0.5)+1):
        pointer = i*2
        while pointer < size:
            sieve[pointer] = False
            pointer += 1
    primes = [i for i in range(size) if sieve[i] == True]
    return primes

LOW_PRIMES = primeSieve(100)
def is_prime(n):
    if n < 2:
        return False
    for prime in LOW_PRIMES:
        if n % prime == 0:
            return False
    return RabinMiller(n)

import random
def RabinMiller(n):
    if not n % 2 or n < 2:
        return False
    if n == 3:
        return True
    s = n - 1
    t = 0
    while not s % 2:
        s //= 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, n-1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != n - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v**2)%n
    return True

def generate_large_prime(keysize=1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**keysize)
        if is_prime(num):
            return num
print(LOW_PRIMES)
print(generate_large_prime())



