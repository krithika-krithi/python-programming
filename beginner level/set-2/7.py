a=input("enter the number")
order=len(str(a))
sum=0
temp=a
while(temp>0):
  b=temp%10
  sum=sum+(b**order)
  temp=temp/10
if(sum==a):
  print("yes")
else:
  print("no")
