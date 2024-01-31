#Python program to interchange first and last elements in a list

#first method
'''l1=[1,2,3,4,5,6,7,8,9]
l1[0],l1[8]=l1[8],l1[0]
print(l1)'''

#second method
'''l1=[1,2,3,4,5,6,7,8,9]
lenn=len(l1)
temp=l1[0]
l1[0]=l1[lenn-1]
l1[lenn-1]=temp
print(l1)'''

