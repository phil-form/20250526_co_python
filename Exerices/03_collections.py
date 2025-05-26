# 1) Initialize an array of 10 integers with the values 
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 using a loop. 
# Then display it.

tab = []

for i in range(10): 
    tab.append(2 ** (i + 1))
    
print(tab)

# 2) Search for a value in an array. 
# If the value is found in the array, display its position

val = int(input("Enter a value to search : "))
length = len(tab)
index = -1
for i in range(length):
    if(val == tab[i]):
        index = i
        
print(index)

# 3) Create an array of random value with random.randint(0, 100)
# and find the smallest value inside that array

import random

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))

length = len(arr)
smallest = arr[0]
for i in range(1, length):
    if(arr[i] < smallest):
        smallest = arr[i]
    
print(smallest)
        

# Create a dictionnary that contains the informations of a person :
# (lastname/firstname/birthdate)

person = {}

person['lastname'] = input("Enter your lastname : ")
person['firstname'] = input("Enter your firstname : ")
person['birthdate'] = input("Enter your birthdate : ")
print(person)


# with datetime
from datetime import datetime

person = {}

person['lastname'] = input("Enter your lastname : ")
person['firstname'] = input("Enter your firstname : ")
person['birthdate'] = datetime.strptime(
    input("Enter your birthdate : "), '%Y/%m/%d'
)
print(person)
