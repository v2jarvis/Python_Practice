#simple example of operator overloading 
class cal:
    def __init__(self,a) -> None:
        self.a=a
    def __mul__(t1,t2):
        return (t1.a*t2.a)
    def __add__(t1,t2):
        return(t1.a+t2.a)
    
t1=cal(5)
t2=cal(10)
print(t2*t1)
print(t1+t2)        