def paper_doll(text):
    text_len = len(text)
    output = ''
    
    for letter in text:
        
        if letter != ' ':
            #print (text, text_len, letter)
            output += letter*3
           
    print(output)
            
paper_doll('this is not worth level 2')