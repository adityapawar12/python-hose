def blackjack(a,b,c):
    total_sum = a+b+c
    if total_sum <= 21:
        return f'this is the total : {total_sum}'
    elif total_sum > 21 and a == 11 or b == 11 or c == 11:
        total_sum -= 10
        return f'this is the total : {total_sum}'
    elif total_sum > 21:
        return 'BUST!'
        
        
result = blackjack(6,8,11)
print(result)
