ram=int(input("Enter Ram Age:"))
shyam=int(input("Enter Shyam Age:"))
mohan=int(input("Enter Mohan Age:"))

if((ram and shyam and mohan) >1 and (ram and shyam and mohan)<110):
    if (ram > (shyam and mohan)):
        print("Ram is Older")
    else:
        if (ram == shyam == mohan):
            print("All have Same Age")
        elif (ram == shyam):
            print("Ram and Shyam have Same Age")
        elif (shyam == mohan):
            print("Shyam and Mohan have Same age")
        elif (ram == mohan):
            print("Ram and Mohan have Same Age")
        elif (shyam > mohan):
            print("Shyam is Older")

        else:
            print("Mohan is Older")
else:
    print("Invalid Age Enter")
