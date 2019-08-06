#d
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(0,k+1):
	s+=l[i]
print(s)
