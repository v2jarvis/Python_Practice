#match string with other string
str1=input("Enter The String1:")
str2=input("ENter The String2:")

for i in str1:
    if(i in str2):
        str2=str2.replace(i,"")
if(len(str2)==0):
    print("True")
else:
    print("False")