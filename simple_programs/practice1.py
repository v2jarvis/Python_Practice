#get a string that have number and alpfhabate and count the second largest

num=int(input("Enter The size:"))
l1=[]
val=input("Enter The Value:")
counts=val.count(" ")
if((counts+1)==num):
    print("Size Equal")
    data=val.split(" ")
    for i in data:
        try:
            temp=int(i)
            l1.append(temp)
        except:
            continue
    l1.sort()
    print(l1[-2])
else:
    print("Wrong Value Input")