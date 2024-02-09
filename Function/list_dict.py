#Write a function that takes a list of integers as input and returns the frequency of each
#number in a dictionary, where the keys are the numbers and the values are their
#frequencies.
def frequency(l1):
    d1={}
    for i in l1:
        d1[i]=d1.get(i,0)+1
    return d1

num=[1,2,2,3,3,3,4,4,4,4]
print(frequency(num))
