#Write a function that takes a string as input and returns a new string with all the vowels removed.
def smart_vowel(s1):
    vowels="aeiouAEIOU"
    val=""
    for i in s1:
        if i not in vowels:
            val+=i
    return val

s1="hello from chetu"
print(smart_vowel(s1))
