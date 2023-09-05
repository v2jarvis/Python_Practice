#find the length of the list
l1=(input("Enter The List Which Are Find Length:-")).split(',')
l1=[int(item) for item in l1]
#l1=[1,2,3,4,5]

#print("The Lenght of List:-",len(l1))

#using native method

temp=0
for i in l1:
    temp=temp+1
print(int(temp))