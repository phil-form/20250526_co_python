# To check a year is a leap year : 
# it needs to be divisible by 4 or 400 but not 100

year = int(input("Enter a year : "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("Is leap year")
else:
    print("Is not a leap year")
