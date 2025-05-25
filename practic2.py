
#create account class with 2 attributes- balance and account no.
#create method for debit, create and printing the balance.


class Account:
    def __init__(self,balance,acc):
        self.balance = balance
        self.acc = acc

    def show_balance(self):
        return "total balance:",self.balance
    
    def debit(self,amount):
        self.balance -= amount
        print("RS.", amount, "was debited")

    def credit(self,amount):
        self.balance += amount
        print("RS.", amount, "was credited")



acc1 = Account(10,12)
acc1.credit(5)
print(acc1.show_balance())
acc1.debit(3)
print(acc1.show_balance())



