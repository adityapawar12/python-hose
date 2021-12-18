def old_macdonald(name):
    for letter in name:
        if name.index(letter) == 0:
            zero = letter.upper()
        elif name.index(letter) == 3:
            three = letter.upper()
        else:
            pass
            
    output = zero + name[1:3] + three + name[4:]
    return output
              
result = old_macdonald('macdonald')
print(result)