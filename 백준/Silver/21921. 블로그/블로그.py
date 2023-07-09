import sys
input = sys.stdin.readline

N , X= map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

if max(arr) == 0:
    print("SAD")
else:
    ans = sum(arr[:X])
    tmp = ans
    cnt = 1

    for i in range(X, N):
        # 슬라이딩 윈도우
        tmp -= arr[i-X]
        tmp += arr[i]

        if tmp > ans:
            ans = tmp
            cnt = 1
        elif tmp == ans:
            cnt += 1

    print(ans)
    print(cnt)