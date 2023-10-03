#self behaviour example
class test:
    def display(self):
        print(self.name,self.add)
    def setval(self,n,a):
        self.name=n
        self.add=a
t1=test()
t2=test()
t1.setval("Niteesh","Noida")
t2.setval("Uday","Noida")
t1.display()
t2.display()
