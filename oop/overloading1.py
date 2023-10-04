#simple example of overloading archive using dispatch lib
from multipledispatch import dispatch

class example:
    @dispatch(int)
    def add(self, a):
        print(a)
    @dispatch(int,float)    
    def add(self,a,b):
        print(a+b)
    @dispatch(float,float)    
    def add(self,a,b):
        print(a-b)
obj=example()
obj.add(4)
obj.add(4.2,2.2)        
obj.add(4,2.2)

