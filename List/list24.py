#simple perform the task 4 occurance in the list
l1=[1,4,[4,3,4,5],[4,5,5,4,4]]
for i in l1:
    if type(i)==list:
        y=(l1.count(4))
        print(y)
