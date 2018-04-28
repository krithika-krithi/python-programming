a=raw_input()
if a.isdigit():
  a=int(a)
  sum=1
  while(a%10!=0):
    a=sum+a
print a
  
  
