a=input()
sum=0
if (a<=0):
  print("enter positive number")
else:
  for i in range(a):
    sum=sum+i
    a-=1
  print sum
  
