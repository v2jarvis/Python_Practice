#simple example of call by val and call by ref

#this is call by value like the changes apply on copy not original
'''def add(x):
    val=x+10
    print(val)
x=5
add(x)
print(x)'''


#this is call by reference the changes apply on orignal one also
'''def add(l1):
    l1.append(6)
    print(l1)

l1=[1,2,3,4,5]
add(l1)
print(l1)'''