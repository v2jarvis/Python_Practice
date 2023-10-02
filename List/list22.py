#find the second minimum elements betwout using any function or method
l1=[2,8,3,1,7,4,6,9,3,5]
max=l1[0]
max1=l1[0]

for i in l1:
    if (i>max):
        max1=max
        max=i
    elif(i>max1 and i!=max):
        max1=i
    if(max1==max):
        print(max1)
