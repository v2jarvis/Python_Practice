#remove nested list
#l1=[1,2,3,[4,5,6,[7,8,9],10,11,12],13,14,15]
#l1=[[1,2,3],[4,5,6]]

def nesrem(l1):
    l2=[]
    for i in l1:
        if type(i)==list:
            l2.extend(nesrem(i))
        else:
            l2.append(i)
    return l2
l1=[1,2,3,[4,5,6,[7,8,9],10,11,12],13,14,15]
val=nesrem(l1)
print(val)