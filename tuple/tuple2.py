#perform multiple task on tuple

'''t1=(10,20,20,23,5,2,90)
#print(t1.count(20)) # for count the value
print(t1.index(20)) #give the value and show the index of it

#find the largest elements in a tuple
#t2=list(t1)
#print(max(t2))'''

t3=('niteesh','uday','sachin',1,2,3,4)
for i in t3:
    if type(i)==int:
        del (t3)
print(t3)





