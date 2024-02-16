#add the value less then 50 and above multiply in the given list
l1=[41,42,49,52,62]

for i in l1:
    if i<50:
        temp=0
        data=i%10
#        print(data)
        val=i-data
        ele=val/10
        temp=data+ele
        print(int(temp))
    else:
        temp=0
        data=i%10
        val=i-data
        ele=val/10
        temp=data*ele
        print(int(temp))


#wrong
'''for i in range(len(l1)):
    if l1[i]<50:
        data=l1[i]%10
        temp+=data
        l2.append(temp)
    else:
        data=l1[i]%10
        temp*=data
        l3.append(temp)
print(l2)'''
