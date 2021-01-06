import decimal_letters_map

def base_to_decimal(source, base):
    destination = 0
    
    decimal_point = source.find(".")
    
    if decimal_point == -1:
        decimal_point = len(source)
        
        destination += sum_of_integral(source[:decimal_point], base)
        
        return destination
    
    else:
        destination += sum_of_integral(source[:decimal_point], base)
        
        destination += sum_of_fractional(source[decimal_point:], base)
    
    return destination

def sum_of_integral(source, base):
    destination = 0
    
    for power in range(0, len(source)):
        if source[::-1][power].isalpha():
            destination += decimal_letters_map.letters_to_decimal(source[::-1][power])  * (base ** power)
        else:
            destination += int(source[::-1][power]) * (base ** power)
    
    return destination

def sum_of_fractional(source, base):
    destination = 0
    
    for power in range(1, len(source)):
        if source[power].isalpha():
            destination += round(decimal_letters_map.letters_to_decimal(source[power])  * (base ** -power), 3)
        else:
            destination += round(int(source[power]) * (base ** -power), 3)
    
    return destination