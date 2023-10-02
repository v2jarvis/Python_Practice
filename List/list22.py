#find the second minimum elements without using any function or method

#l1=input("Enter The List Elements:").split()
l1=[2,8,3,1,7,4,6,9,3,5]
max=l1[0]
max1=l1[0]
max2=l1[0]

for i in l1:
    if (i>max):
        max1=max
        max=i
    elif(i>max1 and i!=max):
        max1=i
    elif(i>max2 and i!=max):
        max2=i
    if(max2!=max):
        pass
print(max)
