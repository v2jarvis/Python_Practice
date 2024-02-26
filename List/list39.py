#add the three digits and above three digit multiply
l1=[100,1002,203,3002]
for i in l1:
    if i>1000:
        temp=0
        rem=i%10
        val=i-rem
        ele=val/1000
        temp=rem*ele
        print(int(temp))
    else:
        temp=0
        rem=i%10
        val=i-rem
        ele=val/100
        temp=rem+ele
        print(int(temp))

