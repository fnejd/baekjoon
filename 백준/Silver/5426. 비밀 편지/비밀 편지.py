import sys
input =sys.stdin.readline

# 테스트 케이스
T = int(input())

for _ in range(T):
    S = input()
    arr = []
    # 정사각형 길이
    N = int(len(S) ** (1/2))

    for x in range(N):
        arr.append(S[x * N : x * N + N])
    
    for j in range(N-1, -1, -1):
        for i in range(N):
            print(arr[i][j], end='')
    print()