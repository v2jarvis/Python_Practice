class Test:
    var=50
    #@classmethod
    def change(cls):
        cls.var=60
        print(cls.var)
obj=Test()
print(obj.var)
# obj.change()
# obj.var=70
# print(obj.var)

