#remove and print the middle occurance elements
l1=[1,2,3,3,3,4,5,5,5,6,7,8,8,8,9,10,10,10]
'''l2=[]
for i in range(len(l1)):
    if(l1.count(i)>1 and l1[i]+1):
        l2.append(l1[i])
print(l2)'''
l1=[1,2,3,3,3,4,5,5,5,6,7,8,8,8,9,10,10,10]
for i in range(len(l1)-1):
    if l1[i-1]==l1[i-2] and l1[i+1]==l1[i+2]:
        print(l1[i])

