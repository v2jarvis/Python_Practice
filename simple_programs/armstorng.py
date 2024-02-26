num=int(input("Enter the number:"))
lenn=len(str(num))
add=0
temp=num
while(temp>0):
    rem=temp%10
    add=add+rem**lenn
    temp=temp//10
if(num==add):
    print("Armstrong")
else:
    print("Not Armstrong")

