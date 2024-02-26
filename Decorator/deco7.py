def smart_add(arg):
    def inner(a,b):
        if a==7:
            a=8
        val=a+b
        return arg(val)
    return inner




@smart_add
def add(val):
    print(val)

add(7,1)