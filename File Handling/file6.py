#use a+ advance file handling and show only new msg
f=open("test4.txt",'a+')
msg=input("Enter The Message:")
f.write(msg)
f.seek(0)
temp=len(f.read())-len(msg)
f.seek(temp)
print(f.read())
f.close()