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
d1={
    'name':'niteesh',
    'age':25,
    'addrs':'noida',
}
#d1.pop('name')
d1.popitem()
print(d1)