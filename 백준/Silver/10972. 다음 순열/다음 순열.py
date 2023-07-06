import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().rstrip().split()))

# 다음 큰 순열 만들기 위해서 뒤에서 앞으로 가면서 앞에 작은 수 있는지 확인
flag = True
for i in range(N-1 ,0, -1):
    # 앞에 더 큰수 있을 경우
    if arr[i-1] < arr[i]:
        for j in range(N-1 ,0, -1):
            if arr[i-1] < arr[j]:
                # swap
                arr[i-1], arr[j] = arr[j], arr[i-1]
                # 뒤에는 제일 작은 순열
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                flag = False
                break
            
    if not flag:
        break

if flag:
    print(-1)