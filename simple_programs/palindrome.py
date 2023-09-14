n=int(input("Enter the number:"))
temp=n
rem=0
while(n>0):
    mod=n%10
    rem=rem*10+mod
    n=n//10
if(temp==rem):
    print("Palindrome")
else:
    print("Not Palindrome")