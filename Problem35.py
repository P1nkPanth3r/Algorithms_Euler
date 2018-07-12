# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from math import sqrt
from itertools import count, islice

def primes_sieve(limit): # Generate all primes below some limit
    limitn = limit+1
    not_prime = set()
    primes = []
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes

cyc_primes = [2,5]
primes = primes_sieve(1000000)
for number in primes:
    string = str(number)
    if ('0' not in string           # Any circular prime cannot include 0, 2, 4, 5, 6, or 8 because at least one
        and '2' not in string       # rotation (the rotation with that number as the last digit) will include a
        and '4' not in string       # composite number (with the exception of 2 and 5 which are included in the initial
        and '5' not in string       # list instantiation). This reduces the search space dramatically.
        and '6' not in string
        and '8' not in string):
        cyc_prime = True        # Assume we have a cyclical prime to start
        for num_char in range(len(string)): # For all rotations of the current number
            number = int(number)
            if number not in primes:
                cyc_prime = False # If we can't find a rotation in the primes list, the number isn't a cyclical prime
            number = str(number)[-1] + str(number)[:-1] # Generate next rotation
        if cyc_prime == True:
            cyc_primes.append(number)
print(len(cyc_primes))

# Approximate solution runtime: 2.866384506225586 seconds