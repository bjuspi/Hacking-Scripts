import decimal_letters_map

def decimal_to_base(decimal, base):
    destination = []
    
    if (decimal == 0):
        return "0"
    
    while (decimal != 0):
        quotient = decimal // base
        remainder = decimal % base
        
        if remainder > 9:
            remainder = decimal_letters_map.decimal_to_letters(remainder)
        
        destination.append(remainder)
        decimal = quotient
        
    destination.reverse()
    destination = [str(i) for i in destination] 
    return "".join(destination)
