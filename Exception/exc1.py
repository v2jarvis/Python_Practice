#zero divisible fix by excp
a=int(input("Enter The Number:"))
b=int(input("Enter The Number:"))

try:
    print(a/b)

except ZeroDivisionError:
    print("Can't divide by zero")