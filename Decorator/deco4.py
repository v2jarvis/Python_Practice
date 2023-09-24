#remove complex and boolean and string from a list

def smart_check(arg):
    def inner(l1):
        l2=[]
        for i in l1:
            if type(i) not in (str,bool,complex):
                l2.append(i)
        return arg(l2)
    return inner

@smart_check
def check_val(l1):
    print(l1)

val = check_val([1, 2, 3, 4, 5, True, False, "niteesh"])
