#Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def val(s1):
    count=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in s1:
        if i in vowels:
            count+=1
    return count

s1="niteesh"
print(val(s1))
