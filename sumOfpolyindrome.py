N = int(input())
 
temp = N
rev = 0
 
while temp != 0:
	rev = (rev * 10) + (temp % 10)
	temp = temp // 10
 
if N == rev:
	print("yes")
else:
	print("no")
