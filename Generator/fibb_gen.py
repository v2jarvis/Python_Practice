#Write a generator function that generates the Fibonacci sequence indefinitely

def fibo():
    a=0
    b=1
    yield a,b

    while True:
        a=b
        b=a+b
        yield b

data=iter(fibo())

print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))




