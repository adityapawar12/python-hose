try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("Division by zero is not possible")
finally:
    print("All Done.")
