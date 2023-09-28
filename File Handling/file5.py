#use advance mode file handling
f=open("test2.html",'w+')
msg=input("Enter The HTML Code:")
f.write(msg)
f.seek(0)
print(f.read())
f.close()
