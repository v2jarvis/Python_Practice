#self use- like object work as a referance pass in self
class sport:
    def run(self):
        print(self,"self")
        print("Running")
obj1=sport()
obj1.run()
print(obj1,"obj1")
