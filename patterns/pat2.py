#simple make pyramid
n=(int(input("Enter the len:")))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")

    for k in range(1,2*i):
        print("*",end="")
    print()
