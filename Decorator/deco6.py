#concatinate the two list using decorator
def smart_add(arg):
    def inner(L1,L2):
        con=L1+L2
        return arg(con)
    return inner

@smart_add
def add(con):
    print(con)

L1 = [1, 2, 4, 5.0, 6.0]
L2 = [7, 8, 9, 10.0]
add(L1,L2)