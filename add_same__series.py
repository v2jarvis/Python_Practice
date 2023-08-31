num=int(input("Enter The Number:"))
add=0
for i in range(1,num+1):
    y=int(str(num)*i)
    print(y)
    add=add+y
print(add)