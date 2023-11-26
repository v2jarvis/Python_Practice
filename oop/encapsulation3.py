# perform the task over private and protected var
class test:
    _p=25 #protected
    __p=35 #private
    #getter
    def get(self):
        return self.__p
    #setter
class test1(test):
    def set(self):
        self.__p=30
        return self.__p

obj=test1()
print(obj.get())
print(obj.set())