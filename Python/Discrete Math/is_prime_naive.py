# -*- coding: utf-8 -*-

def is_prime_naive(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

