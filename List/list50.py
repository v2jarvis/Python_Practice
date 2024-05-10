l1=[1,2,3,4,5,6]
temp=[]
for i in range(len(l1)-1):
    temp.append(l1[i]**2)
temp.append(l1[-1])
print(temp)