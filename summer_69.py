def summer_69(*args):
    ls_args = list(args)
    if 6 in ls_args:
        cut_list_o = ls_args[:ls_args.index(6)]
        cut_list_t = ls_args[ls_args.index(9):]
        final_list = cut_list_o + cut_list_t
        #print(cut_list_o, cut_list_t, final_list)
    
                
    return sum(final_list)
    
    
result = summer_69(1,5,6,8,9,30)
print(result)