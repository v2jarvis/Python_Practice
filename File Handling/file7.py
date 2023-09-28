#read the file and perform the task
f=open("test4.txt",'r+')
print(f.read())
msg=input("Enter The Messages:-")
f.write(msg)
count=0
for i in f.read():
    if(i=='s' or i=='S'):
        count+=1
print(count)
f.close()