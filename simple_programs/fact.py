num=int(input("Enter The Number:-"))
fact=1
if(num==0 or num==1):
    print("The Factorial is:-",1)
else:
    #for i in range(1, num+1):
    #    fact=fact*i
    for i in range(num):
        fact=fact*(i+1)
    print("The Factorial is:-",fact)










