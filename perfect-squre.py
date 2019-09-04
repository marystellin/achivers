import math
N,M=map(int,input().split())
perfect=N*M
root=math.sqrt(perfect)
if int(root+0.5)**2==perfect:
    print("yes")
else:
    print("no")
