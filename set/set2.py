#remove the given element from a set and print assending order
s1={5,1,8,3,7,2,4,9,6}
val=int(input("Enter the value to remove:"))
if val in s1:
    s1.remove(val)
print(s1)