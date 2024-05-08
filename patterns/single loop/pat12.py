'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

num=int(input("Enter the len:"))
for i in range(2*num+1):
    if num>i:
        print(" "*(num-i)+"* "*i)
    else:
        print(" "*(i-num)+"* "*(2*num-i))


    # space=abs(num-i)
    # stars=num-space
    # print(" "*space+" *"*stars)