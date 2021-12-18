import one

one.funcinone()

def funcintwo():
    print("this is the function in two")

print("top level print in two")

if __name__ == "__main__":
    print("two is running directly.")
else:
    print("two is imported")
