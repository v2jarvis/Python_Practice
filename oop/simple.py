#simple oops practice of class and static method
class test:
    @classmethod
    def dis(cls,a):
        print(a**2)
    @staticmethod
    def show(a,b):
        print(a+b)
test.dis(8)
test.show(5,4)