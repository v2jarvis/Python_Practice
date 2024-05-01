#function scope level practice
'''def val():
    global a
    a=a+10
    print(a)

a=5
val()'''


'''a=10
b=20

def outer():
    a=789955
    b=901245
    print(globals()['a'])
    print(globals()['b'])
    print(a)
    print(b)
outer()'''

'''
a=10
def val():
    a=4
    def inner():
        nonlocal a
#       global a
        a=a+10
        print(a)
    return inner()
val()'''

