N= int(input())
list1 = list(map(int,input().split()))[:N]
for i in range(0,N-1,2):
	temp=list1[i]
	list1[i]=list1[i+1]
	list1[i+1]=temp
print(' '.join(str(x)for x in list1))
