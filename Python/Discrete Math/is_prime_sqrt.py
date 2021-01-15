# -*- coding: utf-8 -*-

import math

def is_prime_sqrt(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.pow(n, 0.5))):
        if n%i==0:
            return False
    return True