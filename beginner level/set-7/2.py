n=raw_input()
count =0
for a in n:
	if ((a=='1') or (a=='0')):
		count=count+1
if (count==len(n)):
  print ('yes')
else:
  print ('no') 
