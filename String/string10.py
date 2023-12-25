#reverse a string without using any function or method
s="niteesh"
s2=''
for i in range(len(s)-1,-1,-1):
    s2+=s[i]
print(s2)