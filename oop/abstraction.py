#create simple calculator using of abstraction
from abc import ABC,abstractmethod
class test(ABC):
    @abstractmethod
    def engine(self,a,b):
        pass
class calc(test):
    def engine(self,a,b):
        return a+b

obj=calc()
print(obj.engine(32,23))