#remove string from a list
l1=[1,2,3,"jarvis","niteesh","uday",True,False,4,5,6]
l2=[]
for i in l1:
    if (type(i)!=str):
        l2.append(i)
print(l2)
