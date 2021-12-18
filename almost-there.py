def almost_there(number):
    if number >= 90 and number <= 110:
        return True
    elif number >= 190 and number <= 210:
        return True
    else:
        return False
        
        
result = almost_there(103)
print(result)