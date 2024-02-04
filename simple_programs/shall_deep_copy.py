#practice on shallow copy and deep copy
import copy

#deep copy
a=[1,2,3,4,[6,7,8],9,10]
a1=copy.deepcopy(a)
a1[4][1]=15
print("original:",a)
print("new copy:",a1)

#shallow copy
a=[1,2,3,4,[6,7,8],9,10]
a1=copy.copy(a)
a1[4][1]=-5,-4,-1
print("original:",a)
print("new copy:",a1)
