#using list method
num=int(input("ENter The Number:-"))
fib=[0,1]

for i in range(2,num):
    final=fib[i-1]+fib[i-2]
    fib.append(final)
print(fib)

#normal way simple method
n=int(input("Enter Number:"))
a=0
b=1
for i in range(n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c