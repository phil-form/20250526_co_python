def square(nbr):
    return nbr ** nbr

square(9)

def modify_arr(arr, func):
    for i, val in enumerate(arr):
        arr[i] = func(val)
        
arr = [9, 8, 2, 5, 7, 1, 0]
print(arr)
modify_arr(arr, square)
print(arr)