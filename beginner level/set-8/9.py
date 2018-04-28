import math
a,b=raw_input().split()
a=int(a)
b=int(b)
p= a*b
s= math.sqrt(p)
if p//s==s:
  print ('yes')
else:
  print ('no')
