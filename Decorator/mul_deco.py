#3.	Write a decorator multiply_decorator that multiplies the result of a function by a specified factor.
def multiply_decorator(arg):
    def inner(val):
        data=arg(val)
        res=data*val
        return res
    return inner
@multiply_decorator
def simple(a):
    return a

print(simple(3))

