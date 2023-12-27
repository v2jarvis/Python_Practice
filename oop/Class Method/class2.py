class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

# Usage:
obj1 = MyClass(10)
print(obj1.__init__('value'))
#MyClass.increment_class_variable()
#print(MyClass.class_variable)