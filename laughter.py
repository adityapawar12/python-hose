def laughter(pattern,text):
    pat_len = len(pattern)
    text_len = len(text)
    count=0
    
    for i in range(text_len):
        #print('current index is : ', i)
        for part in text:
            sep_pat = (text[i:pat_len+i])
        #print('current pattern is : ', sep_pat)
        if sep_pat == pattern:
            count +=1
            #print(f'now the count is {count}')
    return f'the number of times this pattern apeared is : {count}'
    
    
result =laughter('hah', 'hahahah')
print(result)