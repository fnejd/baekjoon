N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split(" ")))) 

# 마감 기준 정렬
arr.sort(key= lambda x : x[1])

check = arr[N-1][1] - arr[N-1][0]

for i in range(N-2, -1, -1):
    if arr[i][1] < check:
        check = arr[i][1]
    
    check -= arr[i][0]

if check >= 0 : 
    print(check)
else:
    print(-1)