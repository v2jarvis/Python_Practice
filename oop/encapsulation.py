#create simple example of encapsulation and  implement setter and getter method
class test:
    a=12
    __b=10
    _c=5
    def show(self,a,__b):
        self.a=a
        self.__b=__b

    #getter method
    def get_c(self):
        return self._c
    #setter method
    def set_c(self,val):
        self._c=val


obj=test()
print(obj.a)
print(obj._test__b)
obj1=test()
print(obj1.get_c())
obj2=test()
obj2.set_c(10)
print(obj2.get_c())
