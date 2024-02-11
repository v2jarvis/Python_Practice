#2.	Implement a decorator Remove zero division errordef smart_div(arg):
def smart_div(arg):
    def inner(a,b):
        if(b==0):
            b=1
        return arg(a,b)
    return inner
@smart_div
def div(a,b):
    val=a/b
    print(val)
div(32,0)
