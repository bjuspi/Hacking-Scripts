# -*- coding: utf-8 -*-

def sieve_of_eratosthenes(n):
    eliminated = []
    
    for i in range(2, n+1):
        eliminated.append(False)
    
    prime_list = []
    
    for i in range(2, n+1):
        if not elimin