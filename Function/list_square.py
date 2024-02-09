#Write a function that takes a list of integers as input and returns the sum of the squares
#of all the numbers.
def val(l1):
    temp=0
    for i in l1:
        temp+=i**2
    return temp

num=[1, 2, 3, 4, 5]
print(val(num))