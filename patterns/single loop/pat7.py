'''
    *
   **
  ***
 ****
'''
num=int(input("Enter the len:"))
for i in range(num-1,-1,-1):
    print(" "*(num-i)+"*"*i)
