N = int(input())

dic = {}

for _ in range(N):
    name, curr = input().split(" ")

    if curr == "enter":
        dic[name] = True
    else:
        del dic[name]

# 역순 정렬
res = sorted(dic.keys(), reverse=True)

for k in res:
    print(k)