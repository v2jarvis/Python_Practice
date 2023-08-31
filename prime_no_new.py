num1=int(input("Enter The Number First:"))
num2=int(input("Enter The Number Second:"))

count=0
for i in range(num1,num2):
    flage=False
    for j in range(2,i//2+1):
        if(i%j==0):
            flage=True
            break
    if(flage!=True):
        print(i,end=" ")
        count=count+1
print("Actual Count=",count)

