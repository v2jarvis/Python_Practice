#4.	Create a decorator divider_decorator that prints a horizontal line of dashes before and after executing a function.
def divider_decorator(arg):
    def inner(val):
        print("-"*14)
        data=arg(val)
        print("-"*14)
        return data
    return inner
@divider_decorator
def greet(name):
    print(f"Hello {name}")

greet("niteesh")
