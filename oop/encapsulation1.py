#encapsulation perform on private var
class test:
    __p=3
    def get(self):
        return self.__p
    def set(self,val):
        self.__p=val

obj=test()
print(obj.get())
obj1=test()
obj1.set(10)
print(obj1.get())