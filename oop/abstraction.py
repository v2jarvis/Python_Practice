#create simple calculator using of abstraction
from abc import ABC,abstractmethod
class test(ABC):
    @abstractmethod
    def engine(self,a,b):
        pass
class add(test):
    def engine(self,a,b):
        return a+b
class sub(test):
    def engine(self,a,b):
        return a-b
class mul(test):
    def engine(self,a,b):
        return a*b
class div(test):
    def engine(self,a,b):
        return a/b
obj=add()
print(obj.engine(a=int(input("Enter The add Num:")),b=int(input("Enter The add Num:"))))
obj1=sub()
print(obj1.engine(32,23))
obj2=mul()
print(obj2.engine(32,23))
obj3=div()
print(obj3.engine(32,23))

