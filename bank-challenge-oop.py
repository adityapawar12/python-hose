class Account():

    def __init__(self, owner, balance = 0):

        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt 
        print(f"Added {dep_amt} to the balance.")

    def withdraw(self, wd_amt):
        if (self.balance >= wd_amt):
            self.balance -= wd_amt 
            print("Withdrawal accepted!")
        else:
            print("Sorry not enough funds available.")

    def __str__(self):
        return f"Owner : {self.owner}\nBalance : {self.balance}"


myacc = Account('aditya', 5000)

print(myacc)
myacc.deposit(300)
print(myacc)
myacc.withdraw(500)
print(myacc)
myacc.withdraw(50000)
print(myacc)
