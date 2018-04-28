a,b=raw_input().split()
a=int(a)
b=int(b)
p= a*b
s= p**0.5
if p//s==s:
  print ('yes')
else:
  print ('no')
