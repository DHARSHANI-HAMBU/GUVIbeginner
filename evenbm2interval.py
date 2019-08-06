#d
n,k=map(int,input().split())
l=[]
for i in range(n+1,k):
	if i%2==0:
		l.append(i)
print(*l)
