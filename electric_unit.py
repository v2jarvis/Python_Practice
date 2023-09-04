unit=int(input("Enter The Unit:-"))
choice=int(input("For Home Purpose Press 1 and For Commercial Purpose Press 2:- "))
amt=0
if(choice==1):
    if(unit<100 and unit>0):
        amt=unit*3
        print("The Unit is:-",amt)
    if(unit<200 and unit>100):
        amt=((unit-100)*4)+100*3
        print("The unit is:-",amt)
    if(unit<300 and unit>200):
        amt=((unit-200)*5)+(100*3)+(100*4)
        print("The Unit is:-", amt)
    if(unit<400 and unit>300):
        amt=((unit-300)*6)+(100*3)+(100*4)+(100*5)
        print("The Unit is:-",amt)
    elif(unit>400):
        amt = ((unit - 400) * 7) + (100 * 3) + (100 * 4) + (100 * 5) +(100*6)
        print("The Unit is:-",amt)

elif(choice==2):
    if (unit < 100 and unit > 0):
        amt = unit * 5
        print("The Unit is:-", amt)
    if (unit < 200 and unit > 100):
        amt = ((unit - 100) * 6) + 100 * 5
        print("The unit is:-", amt)
    if (unit < 300 and unit > 200):
        amt = ((unit - 200) * 7) + (100 * 6) + (100 * 5)
        print("The Unit is:-", amt)
    if (unit < 400 and unit > 300):
        amt = ((unit - 300) * 8) + (100 * 7) + (100 * 6) + (100 * 5)
        print("The Unit is:-", amt)
    elif (unit > 400):
        amt = ((unit - 400) * 10) + (100 * 8) + (100 * 7) + (100 * 6) + (100 * 5)
        print("The Unit is:-", amt)

else:
    print("Invalid Choice")