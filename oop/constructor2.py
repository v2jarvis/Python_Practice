#constructor using multilevel inheritance concept
class test:
    def __init__(self,name):
        self.name=name
class test2(test):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
class test3(test2):
    def __init__(self,name,age,mobile):
        super().__init__(name,age)
        self.mobile=mobile

obj=test3("Chetu",23,10015155)
print(obj.name,obj.age,obj.mobile)