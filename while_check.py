num=int(input("Enter The Number:"))
while True:
    print(num)
    num=num+1
    ch=input("Do you want to continue:")
    if(ch!='y' and ch!='Y'):
        print("break")
        break


