# 1) Using a loop, display the multiplication table of 2.

for i in range(10):
    print(2 * (i + 1))
    
for i in range(1, 11):
    print(2 * (i))
    

# 2) Create an algorithm that asks the user for a 
# number and displays as many lines as the number specified by the user.
# Example: the user enters the number 5, and the algorithm displays:
# *
# **
# ***
# ****
# *****

nbr = int(input("Enter a postive number : "))

for i in range(nbr):
    print("*" * i)

# Create a login system using a password. 
# The algorithm asks the user to enter their password. 
# If the correct password is entered, 
# they are greeted. However, if they enter the wrong 
# password three times in a row, a message will inform them that their 
# account is locked and they will not be able to try a fourth time.

password = "12345"
input_pass = ""
errors_count = 0

while input_pass != password and errors_count < 3:
    input_pass = input("Enter the password : ")
    errors_count += 1
    
if(password == input_pass):
    print("Welcome")
else:
    print("Access denied")

# Create the 'Higher or Lower' game.
# The computer randomly chooses a number between 1 and 100. 
# The user is prompted to enter a number, and the algorithm responds with 
# 'It's higher' or 'It's lower'. When the correct number is found, 
# the algorithm displays the number of attempts it took to guess it.

import random

nbr = random.randint(1, 100)
input_nbr = -1

while(nbr != input_nbr):
    input_nbr = int(input("Enter a number"))
    
    if(nbr < input_nbr):
        print("Too big")
    elif(nbr > input_nbr):
        print("Too small")
        
print("You won")