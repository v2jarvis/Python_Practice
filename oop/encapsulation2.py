#one class to other class get the value of private var
class test:
    __p=20
    def dis(self):
        print(self.__p)
class test2(test):
    def show(self):
        super().dis()
obj=test2()
obj.show()