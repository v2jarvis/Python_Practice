prime=int(input("Enter The Number:"))
flag=False
if prime>1:
    for i in range(2,prime//2):
        if(prime%i)==0:
            flag=True
            break
if (flag==True):
    print("Not A Prime Number")
else:
    print("Number is Prime")