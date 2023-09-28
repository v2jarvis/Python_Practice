#create file and input messages again and again
f=open("test.txt",'a')
msg=input("Enter The Text:-")
f.write(msg)
f.close()