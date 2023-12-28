#sort the list without inbuilt method or function
l1=[8,3,1,9,2,5,3,7,6,10,4]

#bubble sort
for i in range(len(l1)):
    for j in range(0,len(l1)-i-1):
        if(l1[j]>l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)