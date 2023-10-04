#create simple hibrid inheritance
class A:
    def greet(self):
        print("Class A ")
class B(A):
    def greet1(self):
        print("Class B")
class C(A):
    def greet1(self):
        print("Class C")
class D(B,C):
    pass

obj=D()
obj.greet()
                