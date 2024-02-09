#Write a function that takes a list of strings as input and returns a new list containing only
#the strings that have more than 5 characters.

def smart_str(l1):
    l2=[]
    for i in l1:
        if len(i)>5:
            l2.append(i)
    return l2

l1=["niteesh","sachin","shaily","uday","alok"]
print(smart_str(l1))
