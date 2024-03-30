#simple lcm program
l1=[2,5,8]
temp=0

if l1[0]>l1[1]:
    temp=l1[0]
elif(l1[1]>l1[2]):
    temp=l1[0]
elif(l1[2]>l1[1]):
    temp=l1[2]
#else:
#    temp=l1[3]

count=0
while(True):
       if (temp%l1[0]==0 and temp%l1[1]==0 and temp%l1[2]==0):
           val=temp
           break
       temp+=1
print(val)











































'''a=75
b=45
temp=0
count=0
if a>b:
    temp=a
else:
    temp=b

while(True):
       if (temp%a==0 and temp%b==0):
           val=temp
           break
       temp+=1
print(val)'''
