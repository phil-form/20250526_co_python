class BankAccount():
    def __init__(self, number, balance, credit_line):
        self.number = number
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
        
    def __str__(self):
        return f'{self.number};{self.balance};{self.credit_line}'
    
    def __repr__(self):
        return f'Account nbr : {self.number}'
    
    def __eq__(self, other):
        # if myBankAccount == otherBankAcount
        if isinstance(other, BankAccount):
            return self.number == other.number
        elif type(other) == object:
            return False
        # if myBankAccount == 500
        elif type(other) == int:
            return self.balance == other
            
        return False
    
class Bank():
    def __init__(self):
        self.accounts = []
        
    def addAccount(self, account):
        self.accounts.append(account)
    
ba = BankAccount(12345, 500, 500)
print(ba == 500) # True 
print(ba.__dict__)
print(ba)

bank = Bank()
bank.addAccount(ba)
print(bank.__dict__)