n=input()
n1 = 1
n2 = 1
count = 0
while count < n:
  print n1,
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count =count+1
