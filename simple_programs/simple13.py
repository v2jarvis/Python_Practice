#perform multiple task on deep copy and shallow copy
from copy import copy, deepcopy
l1 = [1, 2, [3, 5], 4]
# shallow copy
l2 = copy(l1)
l2[3] = 7
l2[2].append(6)

print(l1)
print(l2)

# deep copy
l3 = deepcopy(l1)
l3[3] = 8
l3[2].append(7)
print(l1)
print(l3)
