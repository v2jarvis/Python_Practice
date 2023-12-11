num=int(input("Enter the number:"))
flage=False
for i in range(2,num//2):
    if (num%i==0):
        flage=True
        break
if(flage!=True):
    print("Prime Num")
else:
    print("Not a prime")