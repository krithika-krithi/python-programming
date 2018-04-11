n=10
list=[]
for i in range(n):
  a=input()
  list.append(a)
largest=int()
for large in list:
  if large>largest:
    largest=large
print(largest)
