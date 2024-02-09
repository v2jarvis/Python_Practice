#Write a function that takes a list of strings as input and returns a new list where each
#string is reversed.

def smart_str(l1):
    l2=[]
    for i in l1:
        l2.append(i[::-1])
    return l2

l1=["niteesh","sachin","shaily","uday","alok"]
print(smart_str(l1))
