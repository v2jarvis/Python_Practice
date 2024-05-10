import module_scope

# Accessing global variable from the module
print("Global variable:", module_scope.global_var)

# Calling global function from the module
module_scope.global_function()

# Creating an instance of the GlobalClass defined in the module
obj = module_scope.GlobalClass("Alice")
obj.greet()
