#add the two list using decorator
def smart_add(arg):
    def inner(L1,L2):
        L3=[]
        for i in range(min(len(L1),len(L2))):
            L3.append(L1[i]+L2[i])
        L3.extend(L1[i:]+L2[i:])
        return arg(L3)
    return inner

@smart_add
def add(L3):
    print(L3)
L1 = [1, 2, 4, 5.0, 6.0,"niteesh"]
L2 = [7, 8, 9, 10.0]
add(L1,L2)