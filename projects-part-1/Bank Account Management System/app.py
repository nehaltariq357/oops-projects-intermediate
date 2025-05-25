

class BankAccount:
    def __init__(self,acc,balance):
        self.acc = acc
        self.balance = balance
    
    def deposite(self,amount):
        self.balance +=amount
        deposit_amount = amount
        return "Amount deposited,",deposit_amount,"new balance is:",self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        withdraw_amount = amount
        return "Amount withdrawed,",withdraw_amount,"new balance is:",self.balance
    
    def check_balance(self):
        total_amount = self.balance
        return "total amount:",total_amount

acc2 = BankAccount(11,50)

print(acc2.check_balance())

print(acc2.deposite(60))
print(acc2.check_balance())

print(acc2.withdraw(30))

print(acc2.check_balance())