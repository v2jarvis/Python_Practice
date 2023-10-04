#create constructor using inheritance concept
class test:
    def __init__(self,name):
        self.name=name
class test2(test):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

obj=test2("Chetu",23)
print(obj.name,obj.age)
