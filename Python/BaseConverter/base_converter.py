import decimal_letters_map

def base_to_decimal(source, base):
    destination = 0
    for power in range(0, len(source)):
        if source[::-1][power].isalpha():
            destination += decimal_letters_map.letters_to_decimal(source[::-1][power])  * (base ** power)
        else:
            destination += int(source[::-1][power]) * (base ** power)
    
    return destination