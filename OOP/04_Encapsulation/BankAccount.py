class BankAccount():
    def __init__(self, number, balance, credit_line):
        self.__number = number
        self.__balance = balance
        self.__credit_line = credit_line
        self.__extracts = []
        self.__extracts.append(self.__balance)
    
    # read only, so I declare only a property without a setter    
    @property
    def number(self):
        return self.__number
    
    @property
    def credit_line(self):
        return self.__credit_line
    
    @credit_line.setter
    def credit_line(self, value):
        if(value > 0):
            self.__credit_line = value
    
    @property
    def max_withdraw(self):
        return self.__balance + self.__credit_line
        
    def withdraw(self, amount):
        if(self.__balance - amount > -self.credit_line):
            self.__balance -= amount
        else:
            print("Permission denied")
        self.extracts.append(self.__balance)
            
    def deposit(self, amount):
        if(amount <= 0):
            print("Deposit must be a positive value")
        else:
            self.__balance += amount
        self.extracts.append(self.__balance)
        
ba = BankAccount(12345, 500, 500)
print(ba.__dict__)
ba.__balance = 5
print(ba.__dict__)
# this will call the property def credit_line(self):
print(ba.credit_line)
# this will call the setter def credit_line(self, value):
ba.credit_line = 600