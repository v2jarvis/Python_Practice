#add the number which are have 5
empty=[]
add=0
for i in range(5):
    element=input("Enter The Elements:-")
    empty.append(element)
for j in empty:
    if '5' in j:
        add=add+int(j)
print(add)
