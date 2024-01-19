n, k = map(int, input().split())

arr = list(map(int,input().split()))

cnt = 0
idx=0


for i in range(n-1,0,-1):
    max=arr[i]
    idx=i

    for j in range(0,i):
        if arr[j]>max:
            max=arr[j]
            idx = j

    if arr[i] != arr[idx]:
        arr[i], arr[idx] = arr[idx], arr[i]
        cnt+=1
        if cnt==k:
            print(arr[idx], arr[i])
            exit()

print(-1)