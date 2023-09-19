#0 divisible fix by deco
def smart_div(arg):
    def inner(a,b):
        if (b==0):
            b=1
        return arg(a,b)
    return inner

#cal deco
@smart_div
def div(a,b):
    val=a/b
    print(val)
    return val
div(32,0)
