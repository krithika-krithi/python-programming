a=raw_input()
b=len(a)
b=int(b)
even=''
odd=''
for x in range(1,b+1):
	if(x%2==0):
		even=even+a[x-1]
	else:
		odd=odd+a[x-1]
print odd,even
