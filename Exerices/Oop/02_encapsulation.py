# Improve the BankAccount and add 
# - a account number that is read only
# - make all the attributes private and create a getter/setter 
#   for the credit_line

class BankAccount():
    def __init__(self, number, balance, credit_line):
        self.__number = number
        self.__balance = balance
        self.__credit_line = credit_line
        self.__extracts = []
        self.__extracts.append(self.__balance)
        
    @property
    def number(self):
        return self.__number
    
    @property
    def credit_line(self):
        return self.__credit_line
    
    @credit_line.setter
    def credit_line(self, value):
        self.credit_line = value
        
    def withdraw(self, amount):
        if(self.__balance - amount > -self.__credit_line):
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
        
ba = BankAccount(12345, 500, 500)
ba.withdraw(900)
ba.withdraw(300)
ba.deposit(1000)
print(ba.__dict__)