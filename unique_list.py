def unique_list(lst):
    new_ls = []
    ls= list(lst)
    for item in lst:
        if item not in new_ls:
            new_ls.append(item)
            
    return new_ls
 
new=[1,4,5,4,8,7,9,5,6,1,5]   
res= unique_list(new)
print(res)