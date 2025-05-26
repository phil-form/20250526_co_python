def function_1():
    return 0

def function_2(arg1, arg2, arg3, arg4):
    return arg1 + arg2 * arg3 / arg4

def function_2(arg1, arg2, arg3 = 3, arg4 = 9):
    return arg1 + arg2 * arg3 / arg4

def function_args(*args):
    for arg in args:
        print(arg)
        
function_args("test", "1", "2", "3", "4", "...")
        
def function_array_agr(arr_args):
    for arg in arr_args:
        print(arg)
        
function_args(["test", "1", "2", "3", "4", "..."])

def db_function_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(f'{key} : {val}')

db_function_kwargs(last_name="test", firstname="Test")