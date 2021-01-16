# -*- coding: utf-8 -*-

import math

def is_prime_sqrt(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.pow(n, 0.5))+1):
        if (n%i==0) and (n!=i):
            return False
    return True