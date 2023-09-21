#function that yields cubes of numbers

def cube(num):
    val=(num*num*num)
    yield val
num=int(input("Enter the num to cube:-"))
save=cube(num)
for i in save:
    print(i)

