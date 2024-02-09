#Write a function that takes a string as input and returns True if the string is a palindrome
#(reads the same forwards and backwards), False otherwise.

def check(s1):
    s1=s1.replace(" ", "").lower()
    s2=s1[::-1]
    if(s1==s2):
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

check(input("Enter The String:-"))