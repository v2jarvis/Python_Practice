#Write a function that takes a list of integers as input and returns true if the list is sorted
#in ascending order, False otherwise.

def val(l1):
    for i in range(len(l1)-1):
        if l1[i]>l1[i+1]:
            return False
    return True

l2=[1,2,3,4,5]
l3=[5,4,3,2,1]
print(val(l2))
print(val(l3))
