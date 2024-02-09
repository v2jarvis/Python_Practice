#Write a function that takes two strings as input and returns True if they are anagrams
#(contain the same letters in a different order), False otherwise.

def anagrams(s1,s2):
    s1=s1.replace(" ", "").lower()
    s2=s2.replace(" ", "").lower()
    return sorted(s1)==sorted(s2)

s1="triangle"
s2="integral"
print(anagrams(s1,s2))