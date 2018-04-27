n=input()
a = 1
b= 1
count = 0
while count < n:
  print a,
  temp = a + b
  a= b
  b = temp
  count =count+1
