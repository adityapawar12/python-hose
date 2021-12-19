try:
    f = open('testfile', 'w')
    f.write("this is just sample text.")
except TypeError:
    print("Hey you have a type error")
except OSError:
    print("Hey you have an os error.")
finally:
    print("I always run.")

