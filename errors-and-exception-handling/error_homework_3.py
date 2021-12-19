def ask():

    while True:
        try:
            inp = int(input("Input an integer : "))
        except:
            print("An error occurred! please try again!")
            continue
        else:
            print(f"Thank you, your number squared is : {inp**2}")
            break


ask()
