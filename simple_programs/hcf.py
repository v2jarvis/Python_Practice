#simple hcf
a=15
b=25

temp=0
if a>b:
    temp=a
else:
    temp=b

for i in range(1,temp+1):
    if (a%i==0 and b%i==0):
        print(i)
