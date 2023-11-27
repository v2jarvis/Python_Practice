#add the value and print the series of 2 mul and print the sum
val=int(input("Enter The Val:"))
s1=''
temp=0
add=1
for i in range(val):
    temp+=add
    s1+=str(add)
    add*=2
    if((val-1)==i):
        s1+=" ="
    else:
        s1+="+"
print(s1,temp)
