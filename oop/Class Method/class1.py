#class method practice
class Test:
    salary=20000 #class varriable same for every one
    def __init__(self,name,address):
        self.n=name
        self.a=address
t1=Test('Niteesh','Noida')
t1.salary=25000
print(t1.n,t1.a,t1.salary)
t2=Test('Uday','Noida')
print(t2.n,t2.a,t2.salary)
