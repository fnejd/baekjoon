import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [True for _ in range(N+1)]
cnt = 0

for i in range(2, N+1):
    # 아직 지우지 않은 수
    if arr[i]:
        for j in range(i, N + 1, i):
            # 해당 수를 지우고 아직 지우지 않은 해당 수의 배수 지우기
            if arr[j]: 
                arr[j] = False
                cnt += 1

                if cnt == K:
                    print(j)
                    break
    
