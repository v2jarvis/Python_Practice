#Remove empty List from List
#first and without any predefine function use
l1=[1,2,3,4,5,[],6,7,8,9,[],10,11]

'''for i in l1:
    if(type(i)==list and len(i)>0):
        l1.remove(i)
print(l1)'''

#second method
while [] in l1:
    l1.remove([])
print(l1)


