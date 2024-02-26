#find the second minimum elements without using any function or method.

#l1=input("Enter The List Elements:").split()
l1=[9,8,3,2,2,2,2,2,7,4,6,9,3,5]
min=l1[0]
max=l1[0]
for i in l1:
    if (i>max):
        max=i
max1=max
max2=max

for j in l1:
    if j<min:
        max1=min
        max2=j
    elif(j<max1 and j!=max2):
        max1=j
if(max1!=max2):
    print(max)


#second method
'''for i in range(len(l1)-1,-1,-1):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2[2])'''
