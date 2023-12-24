#simple pyramid second
n=int(input("Enter the len:"))
for i in range(n+1):
    for j in range(1,n-i):
        print("*",end=" ")
    print()