#simple perform the task 4 occurance in the list
'''l1=[1,4,[4,3,4,5],[4,5,5,4,4]]
for i in l1:
    if type(i)==list:
        y=(l1.count(4)-1)
print(y)'''
l1 = [1, 4, [4, 3, 4, 5], [4, 5, 5, 4, 4]]
total_count = 0
skip_first = True

for item in l1:
    if type(item) is list:
        for sub_item in item:
            if sub_item == 4:
                if skip_first:
                    skip_first = False
                else:
                    total_count += 1
    elif item == 4:
        if skip_first:
            skip_first = False
        else:
            total_count += 1

print("Total occurrences of 4 (after skipping the first one):", total_count)
