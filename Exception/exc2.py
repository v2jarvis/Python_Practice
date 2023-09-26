#create three manual exception

class ValidAge(Exception):
    pass
try:
    age=int(input("Enter The Age:"))
    if(age>0 and age<110):
        print("Valid Age")
    else:
        raise ValidAge

except Exception:
    print("Invalid Age")


'''class ValidString(Exception):
    pass

try:
    name=input("Enter The Name:")
    if(type(name)==str):
        print(name)
    else:
        raise ValidString
except Exception:
    print("Take only string input")'''
