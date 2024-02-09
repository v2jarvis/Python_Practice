#Write a function that takes a list of words as input and returns the longest word in the list.
def smart_list(l1):
    return max(l1,key=len)

words=["niteesh","sachin","shaily","uday","alok"]
print(smart_list(words))