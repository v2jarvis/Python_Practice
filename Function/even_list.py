#Write a function that takes a list of integers as input and returns a new list containing
#only the even numbers from the original list.
def num(l1):
    l2=[]
    for i in l1:
        if i%2==0:
            l2.append(i)
    return l2

l1=[1,2,3,4,5,6,7,8,9,10]
result=num(l1)
print(result)
