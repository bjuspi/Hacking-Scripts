# -*- coding: utf-8 -*-

from is_prime_sqrt import is_prime_sqrt

def simple_prime_generation(n):
    prime_list = []
    for i in range(2, n+1):
        if is_prime_sqrt(i):
            prime_list.append(i)
    return prime_list

