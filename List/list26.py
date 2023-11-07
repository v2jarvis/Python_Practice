#count the occurance of 4 and skip the first 4 in the every nested list
l1 = [1, 4, [4, 3, 4, 5], [4, 5, 5, 4, 4]]
for i in l1:
    if(type(i)==list):
        count=0
        for j in range(1,len(i)):
            if(i[j]==4):
                count=count+1
        print(count)

