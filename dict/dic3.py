#perform multiple task on dict
#this simple dict and fecth data using keys and values

'''d1={
    'name':'niteesh',
    'age':25,
    'addrs':'noida',
}
for i in d1.keys():
    print(i)
for j in d1.values():
    print(j)'''
'''
d1={
    'name':'niteesh',
    'age':25,
    'addrs':'noida',
}
#d1.pop('name')
d1.popitem()
print(d1)'''
d1={1:'A',2:'B'}
d2={1:'A',2:'B',3:'C'}
d1.update(d2)
print(d1)
