#creating the class var and perform the multiple task on it
class MyClass:
    class_var = 0  # Class variable

    def __init__(self, value):
        self.class_var = value

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.class_var)
print(obj2.class_var)

MyClass.class_var = 5
print(obj1.class_var)
print(obj2.class_var)
