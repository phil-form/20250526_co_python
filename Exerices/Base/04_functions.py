# 1) Create a function to convert celsius to fahrenheit (˚C * (9/5) + 32 = ˚F)

def convert(deg_c):
    return deg_c * (9/5) + 32

convert(30)

# 2) Recreate the previous exercices with the stars but in a function 
# *
# **
# ...

def print_tree(nbr_lines):
    for i in range(nbr_lines):
        print("*" * (i + 1))

print_tree(7)


# 3) Create a function that takes an array as parameter and compute the mean value of 
# said array

def mean_val(arr):
    total = 0
    length = len(arr)
    for i in range(length):
        total += arr[i]
        
    return total / length

# 4) Create a function that takes 
# two numbers and an operator (+, -, *, /) and returns the result of the operation.
# example : calculator(4, 6, "*")

def calculator(nbr1, nbr2, operator):
    if(operator == "+"):
        return nbr1 + nbr2
    elif(operator == "-"):
        return nbr1 - nbr2
    elif(operator == "*"):
        return nbr1 * nbr2
    elif(operator == "/"):
        return nbr1 / nbr2

def calcultor_2(nbr1, nbr2, operator):
    return eval(f'{nbr1} {operator} {nbr2}')

# 5) Create a funciton that search an element through an array and return its index
# or -1 if the element was not found.

def find_in(arr, needle):
    for i, val in enumerate(arr):
        if(val == needle):
            return i
        
    return -1