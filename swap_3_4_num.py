num1=int(input("Enter Fisrt Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
num4=int(input("Enter Fourth Number:"))

print("Num1:",num1)
print("Num2:",num2)
print("Num3:",num3)
print("Num4:",num4)

num1=num1+num2+num3+num4
num2=num1-(num2+num3+num4)
num3=num1-(num2+num3+num4)
num4=num1-(num2+num3+num4)
num1=num1-(num2+num3+num4)

print("---------------------")
print("After Swap Num1:",num1)
print("After Swap Num2:",num2)
print("After Swap Num3:",num3)
print("After Swap Num3:",num4)
