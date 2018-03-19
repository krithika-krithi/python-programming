a= raw_input()
if a.isdigit():
  num=int(a)
  if(num>0):
	  print("Positive")
  elif(num==0):
	  print("Zero")
  else:
	  print("Negative")
else:
  print("invalid")
