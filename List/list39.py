#add the three digits and above three digit multiply
l1=[100,1112,243,3142]
for i in l1:
    if i>1000:
        mul=1
        temp=i
        while(temp>0):
            rem=temp%10
            mul=mul*rem
            temp=temp//10
        print(mul)
    else:
        add=0
        temp=i
        while(temp>0):
            rem=temp%10
            add=add+rem
            temp=temp//10
        print(add)



    '''if i>1000:
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
        print(int(temp))'''

