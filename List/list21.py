#find the second largest elements without using any function or method
#Naive approach

#using method
'''l1=[2,8,3,1,7,4,6,9,3,5]
sort=set(l1)
s=sorted(sort)
print(s[-2])'''

l1=[2,8,3,1,7,4,6,9,3,5]
'''sort_l1=sorted(l1)

for i in range(sort_l1-2,-1,-1):
    if(l1[i]!=l1[sort_l1-1]):
        print(l1[i])'''

max=l1[0]
max1=l1[0]

for i in l1:
    if (i>max):
        max1=max
        max=i
    elif(i>max1 and i!=max):
        max1=i
    if(max1!=max):
        pass
print(max1)
