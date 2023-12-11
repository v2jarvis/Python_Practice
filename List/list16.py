# manipulate the given list elements
c=['C',0,0,0,0,0]
num=input("Enter The Number:-")
for x in range(len(num)):
    c.pop()
c.extend([num])
for y in c:
    print(y,end="")
