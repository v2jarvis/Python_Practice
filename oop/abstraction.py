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
print(obj.engine(a=int(input("Enter the add num:")),b=int(input("Enter the add num:"))))
obj1=sub()
print(obj1.engine(a=int(input("Enter the sub num:")),b=int(input("Enter the sub num:"))))
obj2=mul()
print(obj2.engine(a=int(input("Enter the mul num:")),b=int(input("Enter the mul num:"))))
obj3=div()
print(obj3.engine(a=int(input("Enter the div num:")),b=int(input("Enter the div num:"))))

