#single level inherirtance
"""class parent:
    def fun1(self):
        print("This is First")


class child(parent):
    def fun2(self):
        print("This is second")


object = child()
object.fun1()
object.fun2()"""

#multiple inheritance
"""class test:
    def fun1(self):
        print("This is First")


class test1:
    def fun2(self):
        print("This is Second")

class test2(test,test1):
    def fun3(self):
        print("This is third")

object = test2()
object.fun1()
object.fun2()
object.fun3()"""

#multi-level inheritance
"""class test:
    def fun1(self):
        print("This is")
class test1(test):
    def fun2(self):
        print("my thrid")
class test2(test1):
    def fun3(self):
        print("example")

object=test2()
object.fun1()
object.fun2()
object.fun3()"""


