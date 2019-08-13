#d
n=input()
a=0
for i in range(0,len(n)):
	a+=n[i]**3
if a==n:
	print("yes")
else:
	print("no")
