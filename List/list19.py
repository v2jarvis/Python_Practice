#find the largest elements betwout using any function or method
l1=[2,8,3,1,7,4,6,9,3,5]

#using method
print(max(l1))

n=len(l1)
mx=l1[0]

for i in range(1,n):
    if (l1[i]>mx):
        mx=l1[i]
print(mx)