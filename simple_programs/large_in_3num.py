num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))

if(num1>num2>num3):
    print("Number First is Greater")
elif(num2>num1>num3):
    print("Number Second is Greater")
else:
    print("Number third is Greater")