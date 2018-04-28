a=input()
m,n=raw_input().split()
m=int(m)
n=int(n)
for i in range(m+1,n):
  if i==a:
    print ('yes')
    break
else:
  print ('no')
    
