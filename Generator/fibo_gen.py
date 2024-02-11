#2.	Write a generator function called fibonacci_sequence that yields the Fibonacci sequence up to a specified number of terms.
def fibbo():
    size=int(input("Enter the size of series:"))
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(size+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    yield a
    yield b

series=iter(fibbo())
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))
