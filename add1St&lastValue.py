N=int(input())
rev=0
fd=0
s=0
ld=N%10
while N>0:
	r=N%10
	rev=rev*10+r
	N=int(N/10)
fd=rev%10
s=fd+ld
print(s)
