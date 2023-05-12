T = int(input())

for _ in range(T):

    N = int(input())

    price = list(map(int, input().split()))

    sell = price[N-1]

    ans = 0

    for i in range(N-1, -1, -1):

        if sell < price[i]:
            sell = price[i]
        else:
            ans += sell - price[i]

    print(ans)