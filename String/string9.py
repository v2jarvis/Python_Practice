#up_low in single word
s1=input("Enter The String:-")
s2=""
for i in range(len(s1)):
    if(i%2==0):
        s2+=s1[i].upper()
    else:
        s2+=s1[i].lower()
print(s2)