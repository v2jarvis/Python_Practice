#Write a generator function that takes a list of strings as input and yields each string reversed.
def rev(l1):
    for i in l1:
        yield i[::-1]

l1=["Niteesh","Pankaj Sir","Yugal","Sachin","Uday"]

data=iter(rev(l1))

print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
