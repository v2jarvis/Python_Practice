#sort the dict without using sort and sorted method
d1={'two':34,'three':25,'one':20}
d2=dict()
l1=list(d1.values())
temp=0
for i in range(len(l1)):
    for j in range(len(l1)):
        if (l1[i]<l1[j]):
            l1[i],l1[j]=l1[j],l1[i]
for k in l1:
    for l in d1:
        if k==d1[l]:
            d2[l]=k
print(d2)

