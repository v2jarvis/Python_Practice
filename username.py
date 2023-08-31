import random as rn
captcha=rn.randint(1000,10000)
user="v2jarvis"
password=123

print("Captcha Code:",captcha)
usr=input("Enter Username:")
pas=int(input("Enter Password:"))
cap=int(input("Enter Captcha Code:"))

if(usr==user and pas==password and cap==captcha):
    print("Login grant")
else:
    print("Encorrect")