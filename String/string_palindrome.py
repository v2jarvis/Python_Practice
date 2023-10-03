l1=(input("Enter The String:-"))
l1=l1.replace(" ", "").lower()

l2=l1[::-1]
if(l1==l2):
    print("String is Palindrome")
else:
    print("String is not Palindrome")