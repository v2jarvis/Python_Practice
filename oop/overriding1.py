#simple example of overriding
class example1:
    def check(self):
        print("example1")
class example2(example1):
    def check(self):
        print("example2")
obj=example2()
obj.check()                
