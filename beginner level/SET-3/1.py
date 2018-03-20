n=input()
a=input()
d=input()
def ap(n,a,d):
  sum=0
  i=0
  while(i<n):
    sum=sum+a
    a=a+d
    i=i+1
  return sum
print(ap(n,a,d))

  
  
