#add 'ing' int the end atleast 3 len if already 'ing' add 'ly' rest print as it is
s1=["niteesh","uday","helloing","he"]
s2=""

for i in s1:
    if len(i)>3:
        if i[-3:]!="ing":
            s2=s2+i+"ing "
for i in s1:
    if i[-3:]=="ing":
        s2=s2+i[:-3]+"ly "
for i in s1:
    if len(i)<3:
        s2+=i
print(s2)