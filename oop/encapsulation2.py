#one class to other class get the value of private var
class test:
    __p=20
    def val(self):
        print(self.__p)


class test1(test):
    def val1(self):
        super().val()

obj=test1()
obj.val1()