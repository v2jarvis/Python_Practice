#create class and add value using method
class test:
    def display(self):
        print(self.name,self.add)
    def set_val(self,n,a):
        self.name=n
        self.add=a

t1=test()
t2=test()
t1.set_val("Niteesh","Noida-63A")
t2.set_val("Uday","Noida")
t1.display()
t2.display()

