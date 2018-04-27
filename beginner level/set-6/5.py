a=raw_input().split()
p=1
for i in a:
  p= p*int(i)
if p%2==0:
  print ('even')
else:
  print ('odd')
