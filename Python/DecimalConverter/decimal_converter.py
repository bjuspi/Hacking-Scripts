# -*- coding: utf-8 -*-

import decimal_letters_map
import math

def decimal_to_base(decimal, base):
    destination = []
    
    if (decimal == 0):
        return "0"
    else:
        decimal_point = str(decimal).find(".")
        if decimal_point == -1:
            integral_part = decimal
            fractional_part = 0
        else:
            integral_part = int(str(decimal)[:decimal_point])
            fractional_part = float(str(decimal)[decimal_point:])
    
    while (integral_part != 0):
        quotient = integral_part // base
        remainder = integral_part % base
        
        if remainder > 9:
            remainder = decimal_letters_map.decimal_to_letters(remainder)
        
        destination.append(remainder)
        integral_part = quotient
    
    destination.reverse()
    
    if (fractional_part == 0):
        destination = [str(i) for i in destination] 
        return "".join(destination)
    else:
        if len(destination) > 0:
            destination.append(".")
        else:
            destination.append("0.")
        
        max_decimal_places = len(str(fractional_part))-2
        decimal_places = 0 
        while ((fractional_part != 0) and (decimal_places < max_decimal_places)):
            result = fractional_part * base
            integer = int(math.modf(result)[1])
            
            if integer > 9:
                integer = decimal_letters_map.decimal_to_letters(integer)
            
            decimal_places += 1
            destination.append(integer)
            fractional_part = round(math.modf(result)[0], 3)
       
    destination = [str(i) for i in destination] 
    return "".join(destination)

decimal_to_base(0.625, 2)
