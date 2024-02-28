#end two element add 12345=9
data=12345
rem1=data%100
val=rem1%10
data=rem1-val
temp=data/10
print(int(temp+val))


