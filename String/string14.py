#In given str print like half of lower and half upper and after space again half of lower and half of upper
from math import *
s1="niteesh kumar yadav".split()
for i in s1:
    for j in range(len(i)):
        if(j<ceil(len(i)/2)):
            print(i[j].upper(), end="")
        else:
            print(i[j].lower(), end="")

    print(end=" ")