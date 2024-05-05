# create simple example of encapsulation and  implement setter and getter method
class Test:
    a=12  # public
    __b=10 # private
    _c=5    # protected

    def show (self, a, __b):
        self.a=a
        self.__b=__b

    #getter method
    def get_c(self):
        return self._c
    #setter method
    def set_c(self,val):
        self._c=val

    def get_b(self):
        return self.__b

    def set_b(self,val):
        self.__b=val

obj=Test()
print(obj.get_b())
obj.set_b(20)
print(obj.get_b())