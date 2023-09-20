# sort a list of tuples using Lambda Original list of tuples
'''tup=([6,4,9,7,5,2,8,3,1],[])
print(tup)
for i in tup:
    if type(i)==list:
        list.sort()
print(tup)'''

'''val=lambda x:x.sort
ele=[6,4,9,7,5,2,8,3,1]
el=[]
for i in ele:
    el.append(i)
print(val(el))'''

l1=[(3, 2), (1, 4), (5, 1), (2, 3)]
new_sort=sorted(l1,key=lambda x:x[0])
print(new_sort)

