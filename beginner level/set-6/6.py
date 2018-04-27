n=raw_input()
d=0
a=0
for i in n:
  if i.isdigit():
    d=1
  elif i.isalpha():
    a=1
if(d==1 and a==1):
  print ('Yes')
else:
  print('No')
