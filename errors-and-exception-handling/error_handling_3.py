def ask_for_int():

    while True:
        try:
            inp = int(input("Please enter a number : "))
        except:
            print("Oops! that is not an number")
            continue
        else:
            print("Thank you!")
            break


ask_for_int()
