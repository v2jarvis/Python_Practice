class Test:
    var=10

    @classmethod
    def change(self,var):
        self.var=var

    def display(cls):
        print(cls.var)

obj=Test()
obj.display()
obj.change(25)
obj.display()
obj.display()
print(Test.var)