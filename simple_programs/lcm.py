#simple lcm program
a=75
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
print(val)
