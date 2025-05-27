# Create a class bank account with the following attributes :
# - current_amount
# - credit_line
# and the following behaviour : 
# - deposit(amount)
# - withdraw(amount)

class BankAccount():
    def __init__(self, balance, credit_line):
        self.balance = balance
        self.credit_line = credit_line
        self.extracts = []
        self.extracts.append(self.balance)
        
    def withdraw(self, amount):
        if(self.balance - amount > -self.credit_line):
            self.balance -= amount
        else:
            print("Permission denied")
        self.extracts.append(self.balance)
            
    def deposit(self, amount):
        if(amount <= 0):
            print("Deposit must be a positive value")
        else:
            self.balance += amount
        self.extracts.append(self.balance)
        
ba = BankAccount(500, 500)
ba.withdraw(900)
ba.withdraw(300)
ba.deposit(1000)
print(ba.balance)
print(ba.credit_line)
print(ba.extracts)