#perform multiple task on constructor
from multipledispatch import dispatch
class test:
    @dispatch(int)
    def __init__(self,a):
        print("Helloo")

    @dispatch(int)
    def __init__(self,a):
        print("Helloo Jarvis")

obj=test(5)
