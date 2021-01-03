# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:34:36 2021

@author: bjusp
"""

def decimal_to_base(decimal, base):
    destination = []
    
    while (decimal != 0):
        quotient = decimal // base
        remainder = decimal % base
        
        destination.append(remainder)
        decimal = quotient
        
    destination.reverse()
    destination = [str(i) for i in destination] 
    return int("".join(destination))
