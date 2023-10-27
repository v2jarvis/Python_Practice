#create simple func and perfom multiple task on that
'''class a:
    def _val(self): #protected method
        return ("hello from jarvis")
class b(a):
    def dis(self):
        val=super()._val()
        print(val)
obj=b()
obj.dis)'''

'''class a:
    def __val(self): #private method
        print("hello from private")
    def val(self):
        return self.__val()
obj=a()
#obj._a__val() #this is call namemangling technique
obj.val() #we can access using creating getter method'''

#method overrriding
class test:
    def first(self):
        return print("hello world")
class test2(test):
    def first(self):
        return print("hello duniya")
class test3(test2):
    def first(self):
        return print("hello jarvis")
obj=test3()
obj.first()