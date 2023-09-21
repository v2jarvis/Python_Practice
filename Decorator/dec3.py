#uper and lower using deco

def take_input(char):
    if (char.islower()):
        char = char.upper()
    elif (char.isupper()):
        char = char.lower()
    return char

def low_up_input(arg):
    def inner(string):
        val=''.join(take_input(char)for char in string)
        return arg(val)
    return inner

'''def lower_input(arg):
    def inner(string):
        y=string.lower()
        return arg(y)
    return inner'''

@low_up_input
def input_str(string):
    print(string)


name=input("Enter the string you wanted to upper and lower:")
input_str(name)
