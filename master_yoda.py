def master_yoda(text):
    rev_text=''
    print('normal people :', text)
    text_list = text.split()
    text_list.reverse()
    for word in text_list:
        rev_text += word + ' '
    print('master yoda be like :', rev_text)
    
master_yoda('you are wise')