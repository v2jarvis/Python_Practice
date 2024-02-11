#3.	Implement a generator function random_password that generates random passwords consisting of uppercase letters, lowercase letters, and digits.
import random
def pass_gen():
    size=int(input("Enter the size of pass:"))
    lowercase="abcdefghijklmnopqerstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQERSTUVWXYZ"
    num="1,2,3,4,5,6,7,8,9,0"

    #l1=[]
    #for i in range(size+1):
    #    l1.append(random.choices(lowercase+uppercase+num))
    #yield l1

    data=lowercase+uppercase+num
    s1= ''.join(random.sample(data,size))
    yield s1



password=iter(pass_gen())
print(next(password))
print(next(password))
print(next(password))
print(next(password))
print(next(password))
print(next(password))
print(next(password))
print(next(password))
