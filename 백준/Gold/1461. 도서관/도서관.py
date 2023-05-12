N, M = map(int, input().split())

books = list(map(int, input().split(" ")))

# 가장 마지막에는 반납하고 돌아오지 않아도 된다
# 갔다가 돌아오는 경우 * 2

# 양수, 음수 분리
neg = []
pos = []


for x in books:
    if x > 0 :
        pos.append(x)
    else:
        neg.append(-x)

# 가장 거리가 먼 책부터 방문하기 위해 내림차순 정렬
pos.sort(reverse=True)
neg.sort(reverse=True)

# 음수 거리의 책이 없거나 양수거리의 책이 없다면 valueError 가 나온다.
# far = max(max(pos), max(neg))


far = max(max(books), -min(books))

ans = 0

for i in range(0, len(pos) , M):
    ans += pos[i] * 2

for i in range(0, len(neg), M):
    ans += neg[i] * 2

# 마지막에는 돌아오지 않아도 된다
print(ans - far)
