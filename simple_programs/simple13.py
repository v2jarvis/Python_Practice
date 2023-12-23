#perform multiple task on deep copy and shallow copy
from copy import copy, deepcopy
'''l1 = [1, 2, [3, 5], 4]
# shallow copy
l2 = copy(l1)
l2[3] = 7
l2[2].append(6)

print(l1)
print(l2)

print(id(l1))
print(id(l2))'''

# deep copy
l1=[1,2,3,[],4,5]
l3 = copy(l1)
l3[5] = 8
l3[3].extend([12,13,14])


print(l1)
print(l3)

print(id(l1))
print(id(l3))