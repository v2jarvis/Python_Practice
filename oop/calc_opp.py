#create method addition/substraction/display
class calc:
    result=0
    
    def add(self,a,b):
        self.result=a+b
    def sub(self,a,b):    
        self.result=a-b    
    def mul(self,a,b):
        self.result=a*b
    def div(self,a,b):
        self.result=a/b    
    def display(self):
        print(self.result)

obj=calc()

obj.add(a=int(input("Enter the number A for add-")),b=int(input("Enter the number B for add-")))
print(obj.result)

obj.sub(a=int(input("Enter the number A for sub-")),b=int(input("Enter the number B for sub-")))
print(obj.result)

obj.mul(a=int(input("Enter the number A for mul-")),b=int(input("Enter the number B for mul-")))
print(obj.result)

obj.div(a=int(input("Enter the number A for div-")),b=int(input("Enter the number B for div-")))
print(obj.result)

