# different way to clear list
#first way
l1=[1,2,3,4,5,6,7,8]
#print(l1.clear())
#print(l1)

#second way
#l1=l1[:0]
#print(l1)

#third way
while(len(l1)!=0):
    l1.pop()
print(l1)

