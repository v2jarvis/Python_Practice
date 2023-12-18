#monkey patching - Monkey patching in Python is a dynamic technique
#that can change the behavior of the code at run-time. In short,
#you can modify a class or module at run-time.
class monkey:
    def patch(self):
        print("patch() being called")
def monk_p():
    print("monk_p() is being called")

monkey.patch=monk_p
obj=monkey
obj.patch()
