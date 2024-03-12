#add three num using operator overloading
class OpTest:
    def __init__(self,val):
        self.val=val
    def __add__(self,add):
        if isinstance(add,OpTest):
            return OpTest(self.val+add.val)
        else:
            return None
num1=OpTest(5)
num2=OpTest(4)
num3=OpTest(5)
#print(num1+num2+num3)
data=num1+num2+num3
print(data.val)

