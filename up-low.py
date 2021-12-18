def up_low(s):
    ups, lows = 0,0
    for letter in s:
        if letter.isupper():
            ups += 1
        elif letter.islower():
            lows += 1
            
    return f'ups : {ups} and  lows : {lows}'
            
            
s='dhsjHEJSjsjHHS'
res = up_low(s)
print(res)