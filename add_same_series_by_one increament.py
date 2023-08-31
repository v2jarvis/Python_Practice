num=int(input("Enter The Number:"))
add=0
for i in range(1,num+1):
    y=int(str(i)*i)
    print(y)
    add=add+y
print(add)