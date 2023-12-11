list1=input("Enter The List Elements:-").split(",")
list2=input("Enter The List Elements:-").split(",")

list3=[]
for i,j in zip(list1,list2):
    output=i+j
    list3.append(output)
print(list3)

