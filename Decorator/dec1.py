#this is first decorator example
def extra(arg):
    def inner():
        print("Hello")
        arg()
        print("See you soon..!!")
    return inner()

#this is the first method to call deco
#@extra
def test():
    print("My name is Niteesh")
#test

#this is the second method to call deco
save=extra(test)
save