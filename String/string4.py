#remove string from a list
l1=[1,2,3,"jarvis",True,False,4,5,6]
for i in l1:
    if (type(i)==str):
        l1.remove(i)
        print(l1)
