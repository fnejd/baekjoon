N, M = map(int, input().split(" "))

dic = {}

for _ in range(N):
    letter = input()
    # 단어 길이가 M을 미만일떄
    if len(letter) < M:
        continue

    # 이미 단어장에 있을 경우
    if letter in dic:
        dic[letter] += 1
    else:
        dic[letter] = 1

# 자주 나오는 단어 정렬, 단어 길이 긴 것 먼저 정렬, 사전순 정렬
res = sorted(dic.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for x in res:
    print(x[0])