#Create a generator function named even_numbers that generates even numbers up to a given limit.

def even():
    num=int(input("Enter the len to generate even num:"))
    for i in range(2,num+1):
        if i%2==0:
            yield i

even=iter(even())
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
