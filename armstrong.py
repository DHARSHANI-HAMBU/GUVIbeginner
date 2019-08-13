#d
def arm(n1):
	d=0
	m=0
	while n1>0:
		d=n1%10
		m+=d*d*d
		n1=n1//10
	return m
n=int(input())
c=arm(n)
if c==n:
	print("yes")
else:
	print("no")
