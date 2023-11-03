#simple find the only odd elements from the mix given list
l1=[12,1,5,5,211,11,111,4,44,4,5,65,5,"niteesh","helloo","from"]
for i in l1:
    if(type(i)==int and i%2==0):
        print(i)
