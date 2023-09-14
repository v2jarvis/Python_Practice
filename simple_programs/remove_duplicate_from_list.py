list=[1,2,3,4,4,5,6,9,9]
new=[]
for i in list:
    if i not in new:
        new.append(i)
print(new)