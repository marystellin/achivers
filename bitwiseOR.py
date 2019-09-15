N = int(input())
arr = list(map(int, input().split()))[:N]
if(N <= 100000):
    for i in range(0, int(N)):
        ans = arr[i] | arr[i+1]
        break
print(ans)
