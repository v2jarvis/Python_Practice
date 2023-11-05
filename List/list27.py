#interchange first and last elements in a list
l1=[4,1,9,5,2,8,3]
le=len(l1)
temp=l1[0]
l1[0]=l1[le-1]
l1[le-1]=temp
print(l1)