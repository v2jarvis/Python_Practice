#capatlized the string without capatlize method

s1=input("Enter the string:")
s2=""
if s1[0].islower():
    val=chr(ord(s1[0])-32)
    s2=val+s1[1:]
print(s2)