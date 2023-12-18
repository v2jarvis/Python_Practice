#read the data on one file and write on second file
f=open('test1.txt','r')
data=f.read()
f1=open('t.txt','w')
f1.write(data)
f.close()
f1.close()