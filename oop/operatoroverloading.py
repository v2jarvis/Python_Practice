#simple example of operator overloading 1
class cal:
    def __init__(self,a) -> None:
        self.a=a
    def __add__(t1,t2):
        return(t1.a+t2.a)
    def __sub__(t1,t2):
        return (t1.a-t2.a)
    def __mul__(t1,t2):
        return (t1.a*t2.a)
    def __truediv__(t1,t2):
        return (t1.a/t1.a)
    
t1=cal(int(input("Enter the fisrt number for add,sub,mul and div:")))
t2=cal(int(input("Enter the second number for add,sub,mul and div:")))
print(t1+t2)
print(t1-t2)
print(t2*t1)
print(t1/t2)
