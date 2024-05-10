# Global variable
global_var = 100

# Global function
def global_function():
    print("This is a global function defined in example_module.py")

# Global class
class GlobalClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# This code will be executed when the module is imported
print("This is printed when the module is imported")
