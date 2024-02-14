#remove elements which are have E or e in the set
s1={"niteesh","value","eval","v2jarvis"}
l1=list(s1)

for i in range(len(l1)-1,-1,-1):
    if 'e' in l1[i]:
        l1.remove(l1[i])
print(l1)