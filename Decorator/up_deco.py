#1.	Create a decorator called uppercase_decorator that converts the result of a function to uppercase.
def uppercase_decorator(arg):
    def inner(string):
        y=string.upper()
        return arg(y)
    return inner

@uppercase_decorator
def input_str(string):
    print(string)

input_str("helloo niteesh")