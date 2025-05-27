# Create two classes SavingsAccount and CurrentAcount 
# both inherit the BankAccount class

# The SavingAccount will track the last withdrawal date and cannot go
# below 0
# The CurrentAccount will use the credit line

# Improve the BankAccount and add 
# - a account number that is read only
# - make all the attributes private and create a getter/setter 
#   for the credit_line

from datetime import datetime

class BankAccount():
    def __init__(self, number, balance):
        self.__number = number
        self.__balance = balance
        self.__extracts = []
        self.__extracts.append(self.__balance)
        
    @property
    def number(self):
        return self.__number
        
    def withdraw(self, amount):
        if(self.__balance - amount > 0):
            self.__balance -= amount
        else:
            print("Permission denied")
        self.__extracts.append(self.__balance)
            
    def deposit(self, amount):
        if(amount <= 0):
            print("Deposit must be a positive value")
        else:
            self.__balance += amount
        self.__extracts.append(self.__balance)

class SavingsAccount(BankAccount):
    def __init__(self, number, balance):
        super().__init__(number, balance)
        self.__last_withdrawal_date = datetime.now
        
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__last_withdrawal_date = datetime.now
        
class CurrentAccount(BankAccount):
    def __init__(self, number, balance, credit_line):
        super().__init__(number, balance)
        self.__credit_line = credit_line
        
    @property
    def credit_line(self):
        return self.__credit_line
    
    @credit_line.setter
    def credit_line(self, value):
        self.__credit_line = value
        
    def withdraw(self, amount):
        if(self.__balance - amount > -self.__credit_line):
            self.__balance -= amount
        else:
            print("Permission denied")
        self.__extracts.append(self.__balance)
    
ba = BankAccount(12345, 500, 500)
ba.withdraw(900)
ba.withdraw(300)
ba.deposit(1000)
print(ba.__dict__)