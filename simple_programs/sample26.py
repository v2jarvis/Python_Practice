#*args, **kwargs meaning in python
def example_function(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

# Call the function with different numbers of arguments
example_function(1, 2, 3, name='Alice', age=30)
