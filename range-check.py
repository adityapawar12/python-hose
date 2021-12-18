def ran_check(num, low, high):
    range_ls = list(range(low, high+1))
    if num in range_ls:
        return f'{num} is in the range between {low} and {high}'
    #return num in range_ls
    
res=ran_check(3,4,5)
print(res)