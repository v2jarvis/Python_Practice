def smartadd(arg):
    def inner(a,b):
        if a+b==8:
            a=8
            b=1
        return arg(a,b)
    return inner

@smartadd
def add(a,b):
    data=a+b
    print(data)
add(7,1)
