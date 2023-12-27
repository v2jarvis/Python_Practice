class a:
    def __val(self): #protected method
        print ("hello from jarvis")
    def show(self):
        self.__val()
class b(a):
    def dis(self):
        super().show()
        #val=self._a__val()
obj=b()
obj.dis()

'''class a:
    def __val(self): #private method
        print("hello from private")
    def val(self):
        return self.__val()
obj=a()
#obj._a__val() #this is call namemangling technique
obj.val() #we can access using creating getter method'''