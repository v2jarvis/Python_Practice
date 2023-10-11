#create multiple inheritance and get the value using parameter
class A:
    def val(self,a):
        self.a=a
        print("Helloo Niteesh")
class B:
    def val(self,a,b):
        self.a=a
        self.b=b
        print("Helloo from jarvis",self.a,self.b)

class C(A,B):
    def val(self,a,b=None):
        if(super().val()):
            print(self.a)
        else:
            print(self.a,self.b)
obj=C()
obj.val(12,1)

