#create simple func and perfom multiple task on that
#method overrriding
class test:
    def first(self):
        return print("hello world")
class test2():
    def first(self):
        return print("hello duniya")
class test3(test2,test):
    def first(self):
        return print("hello jarvis")
obj=test3()
obj.first()

'''
#method overloading
from multipledispatch import dispatch
class a:
    @dispatch(int)
    def first(self,a):
        print("hello world")
    @dispatch(float)
    def first(self,a):
        print("hello duniya")
    @dispatch(int,int)
    def first(self,a,b):
        print("hello jarvis")
    @dispatch(int,float,str)
    def first(self,a,b,c):
        print("hello niteesh")
obj=a()
obj.first(1)'''

'''
from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def dis(self,a,b):
        pass
class b(a):
    def dis(self,a,b):
        print(a+b)
obj=b()
obj.dis(23,2)
'''