# given input - val = "aabbccc"
# output={'a':2,'b':2,'c':3}

val = "aabbccc"
temp={}
for i in val:
    if i in temp:
        temp[i]+=1
    else:
        temp[i]=1
print(temp)

