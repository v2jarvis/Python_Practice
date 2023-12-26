#remove the brackets of nested list but elements stay
l1=[1,2,[3,4,5,6,[7,8,9],10,11],12,13]
'''def engine(l1):
    l2 = []
    for i in l1:
        if (type(i)==list):
            l2.extend(engine(i))
        else:
            l2.append(i)
    return l2

val=engine(l1)
print(val)'''

def engine(l1):
    l2=[]
    for i in l1:
        if type(i)==list:
            l2.extend(engine(i))
        else:
            l2.append(i)
    return l2

val=engine(l1)
print(val)