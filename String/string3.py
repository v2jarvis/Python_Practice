#match string with other string using set
str1=input("Enter The first String:")
str2=input("Enter The Second String:")
val=set(str1).difference(set(str2))
if (len(val)==0):
    print("True")
else:
    print("False")