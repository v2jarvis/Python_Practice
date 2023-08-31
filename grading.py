hindi=int(input("Enter Hindi Marks:"))
english=int(input("Enter English Marks: "))
math=int(input("Enter Math Marks: "))
physics=int(input("Enter Physics Marks: "))
chemistry=int(input("Enter Chemistry Marks: "))

total=hindi+english+math+physics+chemistry
print(total)

prcntge=total/5
print(prcntge)

if(total>=450):
    print("A+")
elif(total>=400):
    print("A")
elif(total>=350):
    print("B+")
elif(total>=300):
    print("B")
elif(total>=250):
    print("C+")
elif(total>=200):
    print("C")
else:
    print("Fail")