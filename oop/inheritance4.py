#create hierarical inheritance and get the value

class chetu:
    def __init__(self,name):
        self.name=name

class skillcentre(chetu):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
class h6(chetu):
    def __init__(self,name,age,mobile):
        super().__init__(name)
        self.age=age
        self.mobile=mobile

obj=h6("Niteesh",17,858585)
print(obj.name,obj.age,obj.mobile)