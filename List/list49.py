#list manipulation problem sort the given elements of list
l1=[714,53,412,32,54]
l2=[]

#for i in range(len(l1)):
for i in l1:
    val=str(i)
    #for j in range(len(str(i))):
    data=[int(i) for i in val]
    for j in range(len(data)):
        for k in range(len(data)):
            if data[j]<data[k]:
                data[j],data[k]=data[k],data[j]
    temp=0
    for l in data:
        temp=temp*10+l
    l2.append(temp)
print(l2)
        #print(str(i)[j])



'''for i in l1:
    temp=i
    stack=0
    while temp>0:
        rem=temp%10
        temp=temp//10
        if rem>temp:
            stack=rem
            temp=stack
            rem=temp
            print(stack)'''