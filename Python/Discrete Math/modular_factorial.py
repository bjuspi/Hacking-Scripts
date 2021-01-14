# -*- coding: utf-8 -*-

def modular_factorial(n, k):
    result = 1
    for i in range(1, n+1):
        result = (result*i)%k
    return result


