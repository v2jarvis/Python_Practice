#always create new file if exist the same name throw error
try:
    f=open("test1.txt",'x')
    msg=input("Enter The Message:")
    f.write(msg)
    f.close()
except FileExistsError:
    print("File Already Exist")
#if exist throw this error
#FileExistsError: [Errno 17] File exists: 'test1.txt'