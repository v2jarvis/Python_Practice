#Write a function that takes a list of strings as input and returns a new list containing the
#strings sorted alphabetically, ignoring case.

def smart_str(l1):
    val=sorted(l1, key=str.lower)
    return val
l1=["Niteesh","Pankaj Sir","Yugal","Sachin","Uday"]
print(smart_str(l1))
