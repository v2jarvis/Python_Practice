#archive overloading using multipledispatch
from multipledispatch import dispatch
class test:
    @dispatch(int,float)
    def add(self,a,b):
        return (a+b)

    @dispatch(int,int)
    def add(self,a,b):
        return (a-b)

    @dispatch(float,float)
    def add(self,a,b):
        return (a*b)

    @dispatch(float,int)
    def add(self,a,b):
        return (a/b)

obj=test()
print(obj.add(2,3.0))
