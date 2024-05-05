from multipledispatch import dispatch
# #practice on  hybrid inheritance
# class test:
#     def fun(self):
#         print("This is First")
#
#
# class test1(test):
#     def fun(self):
#         print("This is Second")
#
# class test2(test):
#     def fun(self):
#         print("This is third")
#
#
# class test3(test1,test2):
#     def fun(self):
#         print("this is fourth")
#
# obj=test3()
# obj.fun()

# class bmw:
#     def engine_rtx(self):
#         print("This is bmd engine")
# class ferrari(bmw):
#     def engine_rtx(self):
#         print("This is ferrari engine")
# class mustang(ferrari):
#     def engine_rtx(self):
#         print("this is mustang engine")
#
# obj=mustang()
# obj.engine_rtx()

# class cal:
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         data=a+b+c
#         return data
#     @dispatch(int,int)
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         data=a+b
#         return data
#
# obj=cal()
# print(obj.add(1,2,4))

#operator overloading
# class test:
#     def __init__(self,val):
#         self.val=val
#     def __add__(self, other):
#         if isinstance(other,test):
#             return self.val+other.val
#         elif isinstance(other,int):
#             return self.val + other
#
# a1=test(2)
# a2=test(4)
# a3=test(3)
#
#
# val=a1+a2
#
# print(a3+val)

class Test:
    def __init__(self,a):
        self.__a=a

    def set_val(self):
        return self.__a
    def get_val(self):
        print (self.__a)

obj=Test(5)
obj.__a=50
obj.get_val()






