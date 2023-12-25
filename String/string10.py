#reverse a string and the list without using any function or method
#s="niteesh"
s=[1,2,3,4,5,6,7,8,9,10]
s2=[]
for i in range(len(s)-1,-1,-1):
    s2.append(s[i])
print(s2)