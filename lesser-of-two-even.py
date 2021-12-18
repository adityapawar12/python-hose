def lesser_of_two_evens(num_1, num_2):
    if num_1 % 2 == 0 and num_2 % 2 == 0:
        
        if num_1 < num_2:
            print(num_1)
        elif num_2 < num_1:
            print(num_2)
    elif num_1 % 2 != 0 or num_2 % 2 != 0:
         if num_1 < num_2:
            print(num_2)
         elif num_2 < num_1:
            print(num_1)
            
         
lesser_of_two_evens(4,2)
lesser_of_two_evens(4,6)
lesser_of_two_evens(4,3)
lesser_of_two_evens(4,9)