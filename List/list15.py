#Remove empty List from List
l1=[1,2,3,4,5,[4,5,5],6,7,8,9,[455],10,11]
for i in l1:
    if(type(i)==list and len(i)>0):
        l1.remove(i)
print(l1)