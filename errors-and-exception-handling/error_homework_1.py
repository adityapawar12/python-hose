try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Provided values are not numbers.")
except:
    print("There is an error!")
