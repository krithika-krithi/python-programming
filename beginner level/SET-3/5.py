a=input()
l=a//2
b=raw_input().split()
b.sort()
if(a%2!=0):
  v=(a-1)/2
  print b[v]
else:
  print ((int(b[l-1])+int(b[l]))//2)
  
