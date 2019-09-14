N,K=map(int,input().split())
factorial1 = 1
for i in range(1,N + 1):
	factorial1 = factorial1*i
result=N-K
factorial2=1
for i in range(1,result + 1):
	factorial2 = factorial2*i
result1=factorial1/factorial2
print(int(result1))
	
