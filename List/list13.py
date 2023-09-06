#reverse a list
#l1=[1,2,3,4,5,6,7,8,9]
#print(l1[::-1])

#second way
#l1.reverse()
#print(l1)

#third way two pointer apporch
l1=[1,2,3,4,5,6,7,8,9]
l=0
r=len(l1)-1

while(l<r):
    temp=l1[l]
    l1[l]=l1[r]
    l1[r]=temp
    l=l+1
    r=r-1
print(l1)
