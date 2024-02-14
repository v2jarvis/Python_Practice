#reverse vowels of a string
s1='hello yugal'
s2=''
vowels='aeiouAEIOU'
l1=[]

for i in s1:
    if i in vowels:
        l1.append(i)

for j in s1:
    if j in vowels:
        s2+=l1.pop()
    else:
        s2+=j
print(s2)
