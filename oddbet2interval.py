#d
n=int(input())
k=int(input())
l=[]
for i in range(n+1,k):
	if i%2==1:
		l.append(i)
print(*l)
