def animal_crackers(text):
     split_words = text.split()
     if split_words[0][0] == split_words[1][0]:
         return True
     else:
         pass
     
result = animal_crackers('okay katl')
print(result)