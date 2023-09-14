name=(input("Enter The Name:"))
desig=input("Enter Designation Type:")
sal=eval(input("Enter Salary:"))
leave=eval(input("Enter Casual Leave:"))

print("***********************")

print("Name:",name)
print("Designation:",desig)

in_tex=0
amt=0

if(sal>50000):
    in_tex=.10*sal
if(leave>2):
    amt=(leave-2)*200

hra=.10*sal
pf=.12*sal
ta=.05*sal
da=.08*sal

print("***********************")

print("HRA:-",hra)
print("Income Tax:-",in_tex)
print("PF:-",pf)
print("Casual Leave Deduction:-",amt)

print("***********************")

print("HRA_TA_DA:-",hra+ta+da)
Gross_Sal=sal+hra+ta+da
Net_Sal=Gross_Sal-(pf+amt+in_tex)

print("***********************")

print("Salary:-",sal)
print("Gross Salary",Gross_Sal)
print("Net Salary:-",Net_Sal)

print("***********************")




