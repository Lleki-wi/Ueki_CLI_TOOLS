# -*- coding: utf-8 -*-

import sys

def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

args = sys.argv
if len(args) != 2:
    print("lprime [integer]")
    exit(1)
n = args[1]
try:
    n = int(n)
except ValueError:
    print("It's not integer")
    exit(1)

print("It's prime" if prime(n) else "It's not prime")
exit(0)