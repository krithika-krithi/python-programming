x=input()
y=input()
for i in range(x,y+1):
	l=len(str(i))
	n=i
	sum=0
	while(n>0):
		a=n%10
		sum=sum+a**l
		n=n//10
	if(sum==i):
		print sum
