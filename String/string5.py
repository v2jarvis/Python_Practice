#remove spacial char and space from a string
s1="niteesh /@#$% yadav"
val=" "
for i in s1:
    if i.isalpha():
        val=val+i
print(val)

#using ascii value
'''for i in s1:
    val=ord(i)
print(val)'''