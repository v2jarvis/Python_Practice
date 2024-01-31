#create three manual exception
class ValidAge(Exception):
    pass
try:
    age=int(input("Enter The Age:"))
    if(age>0 and age<110):
        print("Valid Age")
    else:
        raise ValidAge

except ValidAge:
    print("Invalid Age")

