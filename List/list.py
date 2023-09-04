# remove duplicate elements from the list
#l1=input("Enter The List Elements:-").split(',')

ele=input("Enter The Elements:-")
l1 = [int(x) for x in ele.split(',')]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

