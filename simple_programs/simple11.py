#simple example of global and local namespace
temp = 10
def func():
     temp = 20
     return temp
     #print(temp)
print(temp)
print(func())
print(temp)