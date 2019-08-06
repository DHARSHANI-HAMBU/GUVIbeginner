#d
def prime(n):
	c=0
	for i in range(2,n):
		if n%i==0:
			c+=1
	if c==0:
		a=1
	else:
		a=0
	return a
n,k=map(int,input().split())
l=[]
for i in range(n+1,k):
	if prime(i)==1:
		l.append(i)
print(*l)
