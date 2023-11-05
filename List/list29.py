#count the occurance of any elements in a list
l1=[1,2,4,4,4,4,5,5,5,5,7,7,7,8,9,15,1,4,5,5,16,16]
val=int(input("Enter the count no-"))

'''c=l1.count(val)
print(c)'''

count=0
for i in l1:
    if(i==val):
        count=count+1
print(count)